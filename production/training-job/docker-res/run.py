#!/usr/bin/python
'''
This script is run when the job image is loaded.
'''

import os
import sys
import time
import logging
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s', 
    level=logging.INFO)

# gets env vars + set up MAX_NUM_THREADS
from config import *
# training_utils imports
from utils.trainer import Trainer
from utils.data import get_data, DataBunch

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    
    x, y = get_data(seed=SEED)
  
    # PREPROCESSING
    data = DataBunch(x, y)
    data.process()
    
    # TRAINING 
    trainer = Trainer(data)
    trainer.fit(n_epochs=5)

    
    sys.exit(0)


