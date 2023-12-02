import sys
from os import path

ROOT_DIR = path.dirname(path.abspath(__file__))
sys.path.insert(0, path.join(path.dirname(ROOT_DIR)))

from utils.aocApi import getPuzzleInputFromFile

