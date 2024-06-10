# Real-Time Prediction of Breast Tumor Motion for Image-Guided Radiotherapy using  ConvLSTM Networks
Interdisciplinary Team Project, June 2024, TU/e

# Project Overview
This project aims to develop a machine learning algorithm capable of predicting the position of a breast tumor during radiotherapy sessions, accounting for movement due to human respiration. We have introduced a novel approach using Convolutional LSTM (ConvLSTM) models to predict the next frame in a sequence representing this motion. ConvLSTMs have been proven very successful in next frame prediction as they incorporate the spatial processing of Convolutional Neural Networks (CNNs) and the temporal processing abilities of LSTMs. 

Due to the lack of publicly available MRI data of breast scans during respiration, we implemented data augmentation and synthesis techniques to create realistic motion patterns. The original dataset utilized for this project is available at https://www.cancerimagingarchive.net/collection/advanced-mri-breast-lesions/, which includes segmentation masks for accurate modeling.

# Dataset 
Besides the original data samples that we collected, we created the sequences that include the segmentation masks after being augmented. Each sequence included 20 frames. 

# Data Augmentation
We augment the data by creating a motion that is based on a sinusoidial trajectory. Furthermore, we create synthetic data to enhance the dataset and get better and more representative results. Each image undergoes veertical and horizontal elongation

# Model 
Our model is based on Convolutional Long Short-Term Memory (ConvLSTM) networks, which are suitable for spatiotemporal data. The architecture includes:
  - ConvLSTM Layers: Capture both spatial and temporal dependencies in the data.
  - Conv3D Layers: Export from a sequence of processed frames, the final output.
  - Batch Normalization: Stabilize and accelerate training.
  - Dropout: Prevent overfitting.

# Segmentation 
For our project, we use live MRI images as inputs. To predict tumor motion accurately, it is essential to first segment the tumors. We employ a U-Net architecture for segmentation, using DICE loss as the evaluation metric.

However, due to the limited amount of available data, our model currently struggles to accurately segment the tumors. In future work, we plan to gather more MRI images and fine-tune the model to improve its accuracy.

# Contributors 
- Teresa Hernandez Sabroso (https://github.com/thernansab04)
- Martin Kremnický (https://github.com/martinkremnicky)
- Hilde Kerkhoven (https://github.com/hkerkhoven)
- Christos Michalopoulos (https://github.com/cmichalopoulos2)
