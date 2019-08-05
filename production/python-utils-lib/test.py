import logging
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

from utils.trainer import Trainer
from utils.data import get_data, DataBunch

x, y = get_data(seed=10)
data = DataBunch(x, y)
data.process()

trainer = Trainer(data)
trainer.fit(n_epochs=5)
