# Python utils used across the project
The lib contains 3 main modules:
- **[data.py](./utils/data.py)**: data loading, handling, preprocessing
- **[trainer.py](./utils/trainer.py)**: model training
- **[inference.py](./utils/inference.py)**: model inference for deployment

## Requirements

* Python 3.5+

## Installation

Install via pip:

```bash
pip install --upgrade git+https://github.com/ml-tooling/ml-project-template#subdirectory=production/python-utils-lib
```

or directly from the source code:

```bash
git clone https://github.com/ml-tooling/ml-project-template.git
cd ./production/python-utils-lib/
python setup.py install
```

## Usage

After installation, the package can be imported:

```python
import utils
```
