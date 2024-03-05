# Hackathon Agarvision
![image](https://github.com/MagnusS0/AgarVision_2024/assets/97634880/1e03337a-e5a6-4277-a505-5aea750fbb8e)


This project was developed as part of the AgarVision hackathon hosted by Novo Nordisk at ITU (Denmark). There are two subtasks. 

>first subtask: binary classification of agar plates to determine whether they are empty or not

  Utilizing a pre-trained DenseNet-121 model, originally trained on ImageNet, the project adapts the model for a binary classification task by modifying the last layer. This approach achieved a score of 0.98 (98%) on the final test set based on a combined metric of accuracy and recall.

>second subtask: how many colonies are on each agar plates

Utilizing a pre-trained YOLOv8 model, the project adapts the model for object detection and localization.  The model achieved a score of 0.054 on the final test set based on mean squared log error.

## First subtask: Binary classification
### Setup

1. Clone this repository.
2. Install the required packages by running `poetry install`.
3. Download the dataset [https://agar.neurosys.com/]

### Usage

Open the `binary_classifier.ipynb` notebook and it will go through loading data, preprocessing, model training, and evaluation.

### Performance
The primary goal of the model was to minimize false negatives to ensure that agar plates with bacteria are accurately identified, avoiding the risk of misclassifying contaminated plates as clean. In the validation set, out of 198 agar plates that were truly empty, the model correctly identified 187, resulting in 11 false negatives. This translates to an approximately 4% misclassification rate for the empty class.


![image](https://github.com/MagnusS0/AgarVision_2024/assets/97634880/4cacb10e-8389-4f25-b5aa-7716c0af47ff)

## Second Subtask: Object detection
### Setup
Install the required packages
```bash
pip install ultralytics
```
### Usage 
Since we run models on a cluster, we have to submit jobs to the cluster. The following scripts are used to submit jobs to the cluster. You might need to change the paths to the data and the model as well as the required resources in the bash scripts.
- **Process the data:**
We turn all the images into grayscale and resize them since they are in different lighting conditions and sizes.
```bash
sbatch data.sh
```
- **Train the model**: you might need to change the setting in `novo.yaml`.
```bash
sbatch sbatch.sh
```
- **Evaluate the model**
```bash
sbatch eval.sh
```