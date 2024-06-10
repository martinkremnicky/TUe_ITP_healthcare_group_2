# TUe_ITP_healthcare_group_2

# Project Overview
This project aims to develop a machine learning algorithm capable of predicting the position of a breast tumor during radiotherapy sessions, accounting for movement due to human respiration. We have introduced a novel approach using Convolutional LSTM (ConvLSTM) models to predict the next frame in a sequence representing this motion.

Due to the lack of publicly available MRI data of breast scans during respiration, we implemented data augmentation and synthesis techniques to create realistic motion patterns. The original dataset utilized for this project is available at https://www.cancerimagingarchive.net/collection/advanced-mri-breast-lesions/, which includes segmentation masks for accurate modeling.
