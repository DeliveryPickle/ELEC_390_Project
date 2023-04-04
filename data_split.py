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
            j = size-1
        outList.append(data[i:j])
        i = j
    return outList # outputs an array of the split up intervals

# np.save("data",'')
output = {}

filePath = ["WalkingFrontPocket.csv", "WalkingBackPocket.csv", "WalkingCoatPocket.csv", "WalkingArmsUp.csv", "WalkingArmsDown.csv", "JumpingFrontPocket.csv", "JumpingBackPocket.csv", "JumpingCoatPocket.csv", "JumpingArmsUp.csv", "JumpingArmsDown.csv"]

for i in filePath:
    matrix1 = pd.read_csv("Elise/" + i)
    temp = data_split(matrix1)
output = np.append(output, temp)

for i in filePath:
    matrix1 = pd.read_csv("Simon/" + i)
    temp = data_split(matrix1)
output = np.append(output, temp)

for i in filePath:
    matrix1 = pd.read_csv("Lucas/" + i)
    temp = data_split(matrix1)
# output = np.load("data.npy", allow_pickle=True)
output = np.append(output, temp)

# np.save("data", temp)

np.random.shuffle(output)

training = output[0:math.floor(len(output)*0.9)] # from 0 to 90% of the shuffled data
testing = output[math.floor(len(output)*0.9):] # from 90% to the end of the shuffled data
# print(training, '\n')
# print(testing)

with h5py.File('./ELEC390_Data.h5', 'w') as hdf:
    Data = hdf.create_group('/Dataset')
    Training = Data.create_group('Training')
    for i in range(0, len(training)):
        #print(training[i])
        Training.create_dataset('Training Data '+str(i), data=training[i])

    Testing = Data.create_group('Testing')
    for i in range(0, len(testing)):
        Testing.create_dataset('Testing Data '+str(i), data=testing[i])
