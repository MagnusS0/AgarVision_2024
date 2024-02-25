# Hackathon Agarvision
![image](https://github.com/MagnusS0/AgarVision_2024/assets/97634880/1e03337a-e5a6-4277-a505-5aea750fbb8e)


This project was developed as part of the AgarVision hackathon hosted at ITU (Denmark) and focuses on the binary classification of agar plates to determine whether they are empty or not. Utilizing a pre-trained DenseNet-121 model, originally trained on ImageNet, the project adapts the model for a binary classification task by modifying the last layer. This approach achieved a score of 0.98 (98%) on the final test set based on a combined metric of accuracy and recall.


## Setup

1. Clone this repository.
2. Install the required packages by running `poetry install`.
3. Download the dataset [https://agar.neurosys.com/]

## Usage

Open the `binary_classifier.ipynb` notebook and it will go through loading data, preprocessing, model training, and evaluation.

## Performance
The primary goal of the model was to minimize false negatives to ensure that agar plates with bacteria are accurately identified, avoiding the risk of misclassifying contaminated plates as clean. In the validation set, out of 198 agar plates that were truly empty, the model correctly identified 187, resulting in 11 false negatives. This translates to an approximately 4% misclassification rate for the empty class.


![image](https://github.com/MagnusS0/AgarVision_2024/assets/97634880/4cacb10e-8389-4f25-b5aa-7716c0af47ff)

