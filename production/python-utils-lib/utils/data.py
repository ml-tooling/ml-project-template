import logging
logger = logging.getLogger(__name__)
import numpy as np
from tqdm import tqdm
import time

def get_data(seed=1337):
    np.random.seed(seed)
    return np.random.randn(10), np.random.randint(2, size=10)

class DataBunch():
    def __init__(self, x,y):
        self.x, self.y = x, y 
    
    def process(self, func = lambda x:x):
        # data preprocessing
        logger.info(f"Pre-processing {len(self.x)} entries")
        for i in tqdm(range(len(self.x))):
            self.x[i] = func(self.x[i])
            time.sleep(0.1)
