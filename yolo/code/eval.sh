#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --job-name=hc
nvidia-smi
CUDA_LAUNCH_BLOCKING=1 python eval.py