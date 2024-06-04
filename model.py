import torch
import torch.nn as nn

class DoubleConvBlock(nn.Module):
    """ Convolutional block for U-Net.

    it consists of two convolutional layers with batch 
        normalization followed by a ReLU activation function.
    """

    def __init__(self, in_channels, out_channels, kernel_size = 3): #-> None:
        """ Initializes double_conv_block with specified input and output channels,
                kernel size, and padding.
        """
        super(DoubleConvBlock, self).__init__()
        self.conv = nn.Sequential(
                            nn.Conv2d(in_channels, out_channels, kernel_size, padding='same'),
                            nn.BatchNorm2d(out_channels),
                            nn.ReLU(inplace=True),
                            nn.Conv2d(out_channels, out_channels, kernel_size, padding='same'),
                            nn.BatchNorm2d(out_channels),
                            nn.ReLU(inplace=True)
                            )
        
    def forward(self, x): #-> torch.Tensor:
        return self.conv(x)

class Encoder(nn.Module):
    """Encoder part of U-Net.

    This consists of a series of convolutional blocks followed by 
        maxpooling operations..

    Args:
        channels (List[int]): A list of channels for convolutionals block.
                >>>channels = [1, 64, 128, 256, 512, 1024]

    """

    def __init__(self, channels): #-> None:
        super(Encoder, self).__init__()
        self.encoder_blocks = nn.ModuleList()

        # Add a convolutional block followed by maxpooling(except last one) for each level
        for i in range(len(channels)-1):
            self.encoder_blocks.append(
                DoubleConvBlock(channels[i], channels[i+1])),

            # Add a max pooling layer after each convolutional block except the last one
            if i < len(channels)-2:
                self.encoder_blocks.append(nn.MaxPool2d(kernel_size=2))

    def forward(self, x): #-> list[torch.Tensor]:
        encoder_features = []
        for encoder_block in self.encoder_blocks:
            x = encoder_block(x)

            # Save the output of each convolutional block
            if isinstance(encoder_block, DoubleConvBlock):
                encoder_features.append(x)

        return encoder_features


class Decoder(nn.Module):
    """Decoder of the U-Net.

    This consists of a series of convolutional blocks with decreasing number of channels.

    Args:
        channels (List[int]): A list of channels for convolutionals block.
                >>>channels = [1024, 512, 256, 128, 64]
                                            
    """

    def __init__(self, channels): #-> None:
        super(Decoder, self).__init__()
        self.decoder_blocks = nn.ModuleList()

        # Add a upconvolutional followed by a double convolutional block for each level
        for i in range(len(channels)-1):
            self.decoder_blocks.append(nn.ConvTranspose2d(
                channels[i], channels[i+1], 2, 2))
            self.decoder_blocks.append(
                DoubleConvBlock(channels[i], channels[i+1]))

    def _center_crop(self, feature, target_size): #-> torch.Tensor:
        """Crops the input tensor to the target size.
        
        Args:
            feature (torch.Tensor)
            target_size (torch.Tensor)
            
        Returns: 
            cropped feature (torch.Tensor)
        """
        _, _, H, W = target_size.shape
        _, _, h, w = feature.shape

        # Calculate the starting indices for the crop
        h_start = (h - H) // 2
        w_start = (w - W) // 2

        # Crop and returns the tensor
        return feature[:, :, h_start:h_start+H, w_start:w_start+W]

    def forward(self, x, encoder_features): #-> torch.Tensor:

        for i, decoder_block in enumerate(self.decoder_blocks):

            # Concatenate the output of the encoder with the output of the decoder
            if isinstance(decoder_block, DoubleConvBlock):
                encoder_feature = self._center_crop(encoder_features[i//2], x)
                x = torch.cat([x, encoder_feature], dim=1)

            # Apply the upconv or double convolutional block
            x = decoder_block(x)
        return x

class UNet(nn.Module):
    """The UNet architecture.   

    Args:
        out_channels (int): The number of output channels.
        channels (List[int]): A list of channels for convolutionals block.

    Example:
        >>> model = UNet(channels=[1, 64, 128, 256, 512], out_channels=1)
    """

    def __init__(self, channels, out_channels): #-> None:
        super(UNet, self).__init__()
        self.encoder = Encoder(channels)
        self.decoder = Decoder(channels[::-1][:-1])
        self.output = nn.Conv2d(channels[1], out_channels, kernel_size=1)

    def forward(self, x): #-> torch.Tensor:
        encoder_features = self.encoder(x)[::-1]
        x = self.decoder(encoder_features[0], encoder_features[1:])
        x = self.output(x)
        return x
