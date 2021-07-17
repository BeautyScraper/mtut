from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re

from mutv1 import frad

frad()
frad('*.mp4')
frad('*.ts')
frad('*.TS')