import csv
import numpy as np
import math
from sklearn.model_selection import train_test_split
#import h5py

def data_split(data):
    outList = []
    gap = 0
    i = 1
    j = 1
    size = len(data)
    diff = data[-1][0] - data[1][0]
    gap = int(size//(math.ceil(diff/5)))
    while j < size-1:
        j = j + gap
        if j >= size:
            j = size-1
        outList.append(data[i:j])
        i = j
    return outList

with open('Accelerometer.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
matrix1 = np.matrix(spamreader)
matrix1 = my_data = np.genfromtxt('Accelerometer.csv', delimiter=',')
temp = data_split(matrix1)

print(len(temp))
print(temp[0])