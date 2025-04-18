#!/usr/bin/env bash

CONFIG=$1

python -m torch.distributed.launch --nproc_per_node=1 --master_port=4321 basicsr/train.py -opt $CONFIG --launcher pytorch
# torchrun --nproc_per_node=1 train.py --opt Denoising/Options/RealDenoising_Restormer.yml