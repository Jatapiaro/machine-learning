#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:20:28 2022

@author: jacobo
"""

import pandas as pd

SAMPLE_DATA_PATH = '/usr/datasets/Part1_DataPreprocessing/Section2/Data.csv'

def load_dataset(path = SAMPLE_DATA_PATH, ):
    dataset = pd.read_csv(filepath_or_buffer=path)
    # independent variable vector (x)
    x = dataset.iloc[:, start_col:end_col].values
    
    # dependent variable vector (y)
    y = dataset.iloc[:, ]

    return x, y
    

def main():
    x, y = load_dataset(path=SAMPLE_DATA_PATH)
    print(x)

if __name__ == "__main__":
    main()


