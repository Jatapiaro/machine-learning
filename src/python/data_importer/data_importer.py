#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:20:28 2022

@author: jacobo
"""

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer

SAMPLE_DATA_PATH = '/usr/datasets/Part1_DataPreprocessing/Section2/Data.csv'

def load_dataset(path = SAMPLE_DATA_PATH, x_iloc_callback = None, y_iloc_callback = None, x_imputer_callback = None, imputer = None):
    if x_iloc_callback is None or y_iloc_callback is None:
        raise Exception('A callback function to set the x or y vectors is needed')

    dataset = pd.read_csv(filepath_or_buffer=path)
    # Independent variables
    x = x_iloc_callback(dataset)

    # Dependent variables
    y = y_iloc_callback(dataset)

    if imputer is None:
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

    if not x_imputer_callback is None:
        x = x_imputer_callback(x, imputer)

    return x, y

def x_imputer_callback(vector, imputer):
    vector[:, 1:3] = imputer.fit_transform(vector[:, 1:3])
    return vector

def main():
    x_iloc_callback = lambda dataset: dataset.iloc[:, :-1].values
    y_iloc_callback = lambda dataset: dataset.iloc[:, 3].values

    x, y = load_dataset(
        path=SAMPLE_DATA_PATH, 
        x_iloc_callback=x_iloc_callback, 
        y_iloc_callback=y_iloc_callback, 
        x_imputer_callback=x_imputer_callback,
    )

    print(x, y)

if __name__ == "__main__":
    main()


