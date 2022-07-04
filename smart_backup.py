import numpy as np
import shutil
import pandas as pd
from pathlib import Path
from mutv1 import dir_to_list,fileListCopy
from random import shuffle,randint

csv_file_path = r'backup.csv'

def validate(src_dir,dst_dir):
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)
    if not src_dir.is_dir():
        input(f'{src_dir} is not a valid/existing dir')
        raise 'src does not exist'
    if not dst_dir.is_dir():
        input(f'{dst_dir} is not a valid/existing dir do you want to copy into the right hdd')
        dst_dir.mkdir(exist_ok=True,parents=True)


def copy_perc(src_dir,dst_dir,percentage=100):
    validate(src_dir,dst_dir)
    sel_count = int((total_length * percentage)/100)
    if sel_count == 0:
        return
    file_list = dir_to_list(src_dir)
    total_length = len(file_list)
    if percentage < 100:
        shuffle(file_list)
    fileListCopy(file_list[:sel_count], dst_dir)

def main():
    df = pd.read_csv(csv_file_path)
    for index,row in df.iterrows():
        copy_perc(row['Destination'], row['Source'], 100)
        copy_perc(row['Source'], row['Destination'], int(row['percentage']))


if __name__ == '__main__':
    main()

