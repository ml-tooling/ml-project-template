import sys
import time
from tqdm import tqdm

if __name__ == "__main__":
    
    # TRAINING 

    for i in tqdm(range(10), desc="training"): 
        time.sleep(0.2)
    
    print("Training is finished.")
    
    sys.exit(0)
