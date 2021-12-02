import os, sys
import random

import numpy as np
import pandas apd 

import torch

def fix_seeds(seed=42, use_torch=False, multi_gpu=False):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    if use_torch:
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True

    if multi_gpu:
        torch.cuda.manual_seed_all(RANDOM_SEED) #FOR MULTI-GPU

 
def make_directory(path):
    os.makedirs(f'{path}', exist_ok=True)
    
    
