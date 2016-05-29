#from experiment import Experiment
import os

def _save_path(*args):
    return os.path.join(*args)

PACKAGE_DIR = _save_path(os.path.dirname(__file__))
PROJECT_DIR = _save_path(os.path.dirname(PACKAGE_DIR))
DATA_DIR = _save_path(PACKAGE_DIR, 'data')
SPECIMENS_DIR = _save_path(DATA_DIR, 'specimens')
EXPERIMENTS_DIR = _save_path(DATA_DIR, 'experiments')
