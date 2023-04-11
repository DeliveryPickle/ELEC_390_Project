import csv
import numpy as np
import math
import pandas as pd
from sklearn.model_selection import train_test_split
import h5py
import matplotlib.pyplot as plt
import numpy as np
import data_split
import classifier

def fillFrame(data):
    data = data_split.data_split(data)
    outList = pd.DataFrame()
    for i in data:
        if i.loc[:,'type'].sum() > len(i)/2:
            i.loc[i['type'] == 0, 'type'] = 1
        else:
            i.loc[i['type'] == 1, 'type'] = 0
        outList = pd.concat([outList,i])
    print(outList)
    return outList



# fileName = "JumpingArmsDown.csv"
# df = pd.read_csv(fileName)
# df = classifier.classify_input(df)
# df = df.reset_index(drop=True)
# df = fillFrame(df)
# print(df)