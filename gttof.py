from pathlib import Path
# from MyUtility import fileListCopy
import sys
# import pandas as pd
# from random import shuffle
import random
# import numpy as np
import os
import re
# import cv2
import shutil 
import argparse
from mutv1 import fileListCopy
# import subprocess

def doIt(dirPath,Extension,outDirPath):
    fileList = [str(x) for x in dirPath.rglob(Extension)]
    fileListCopy(fileList,str(outDirPath))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirPath', type=Path,default=Path.cwd())
    parser.add_argument('--outPath', type=Path,default=Path.cwd() / 'files')
    parser.add_argument('--exts', nargs='+')
    args = parser.parse_args()
    print(args.exts)
    # import pdb;pdb.set_trace()
    for extension in args.exts:
        doIt(args.dirPath,extension,args.outPath)
    





