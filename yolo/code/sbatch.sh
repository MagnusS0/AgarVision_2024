#!/bin/bash
#SBATCH -p gpu --gres=gpu:1
#SBATCH --job-name=hc
nvidia-smi
yolo train data=novo.yaml model=yolov8s.pt epochs=20 imgsz=640 batch=16