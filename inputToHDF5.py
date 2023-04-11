import csv
import numpy as np
import math

import pandas as pd
from sklearn.model_selection import train_test_split
import h5py

# accepts matrices and lists, splits them into 5 second intervals
def data_split(data):
    outList = []
    gap = 0
    i = 1
    j = 1
    size = len(data)
    diff = data.iloc[-1][0] - data.iloc[1][0]
    gap = int(size//(math.ceil(diff/5)))
    while j < size-1:
        j = j + gap
        if j >= size:
            break #j = size-1
        outList.append(data[i:j])
        i = j
    return outList # outputs an array of the split up intervals

output = []

filePath = ["WalkingFrontPocket.csv", "WalkingBackPocket.csv", "WalkingCoatPocket.csv", "WalkingArmsUp.csv", "WalkingArmsDown.csv", "JumpingFrontPocket.csv", "JumpingBackPocket.csv", "JumpingCoatPocket.csv", "JumpingArmsUp.csv", "JumpingArmsDown.csv"]
j = 0
for i in filePath:
    matrix1 = pd.read_csv("Elise/" + i)
    if j <= 4:
        matrix1["Type"] = 0
        temp = data_split(matrix1)
    else:
        matrix1["Type"] = 1
        temp = data_split(matrix1)
    j += 1
    for i in temp:
        output.append(i)
j = 0
for i in filePath:
    matrix1 = pd.read_csv("Simon/" + i)
    if j <= 4:
        matrix1["Type"] = 0
        temp = data_split(matrix1)
    else:
        matrix1["Type"] = 1
        temp = data_split(matrix1)
    j += 1
    for i in temp:
        output.append(i)
j = 0
for i in filePath:
    matrix1 = pd.read_csv("Lucas/" + i)
    if j <= 4:
        matrix1["Type"] = 0
        temp = data_split(matrix1)
    else:
        matrix1["Type"] = 1
        temp = data_split(matrix1)
    j += 1
    for i in temp:
        output.append(i)

#training, testing = train_test_split(output, test_size=0.1, shuffle=True, random_state=0)
np.random.shuffle(output)
training = output[0:math.floor(len(output)*0.9)] # from 0 to 90% of the shuffled data
testing = output[math.floor(len(output)*0.9):] # from 90% to the end of the shuffled data
with h5py.File('./ELEC390_Data.h5', 'w') as hdf:
    Data = hdf.create_group('/Dataset')
    Training = Data.create_group('Training')
    for i in range(0, len(training)):
        temp = pd.DataFrame(training[i])
        temp = temp.astype(np.float64)
        Training.create_dataset('Training Data '+str(i), data=temp)

    Testing = Data.create_group('Testing')
    for i in range(0, len(testing)):
        temp = pd.DataFrame(testing[i])
        temp = temp.astype(np.float64)
        Testing.create_dataset('Testing Data '+str(i), data=temp)
