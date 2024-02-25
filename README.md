# Hackathon Agarvision

This project was developed as part of the AgarVision hackathon and focuses on the binary classification of agar plates to determine whether they are empty or not. Utilizing a pre-trained DenseNet-121 model, originally trained on ImageNet, the project adapts the model for a binary classification task by modifying the last layer. This approach achieved a score of 0.98 (98%) on the final test set based on a combined metric of accuracy and recall.

## Setup

1. Clone this repository.
2. Install the required packages by running `poetry install`.
3. Download the dataset

## Usage

1. Use the `binary_classifier.ipynb` notebook for the binary Densenet-121 classifier.