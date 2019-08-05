import time
import logging
logger = logging.getLogger(__name__)
from tqdm import tqdm

class Trainer():

    def __init__(self, data):
        self.data = data
        logger.info("Trainer has been initialized")

    def fit(self, n_epochs=3):
        for i in tqdm(range(n_epochs), desc="training epochs"):
            time.sleep(0.25)
        logger.info("Finished training")
