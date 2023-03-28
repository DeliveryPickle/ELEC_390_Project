import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

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
    return outList

matrix1 = pd.read_csv("Raw Data.csv")
matrix2 = pd.read_csv("JumpingBackPocket.csv")
temp = data_split(matrix1)
dataset1 = temp[0]
temp = data_split(matrix2)
dataset2 = temp[0]

window_size = 71
dataset1_sma = dataset1.rolling(window_size).mean()
dataset2_sma = dataset2.rolling(window_size).mean()
fig, ax = plt.subplots(2, 2)
dataset1.plot(x = "Time (s)",ax=ax.flatten()[0:5],subplots=True, sharex=False)
fig, ax = plt.subplots(2, 2)
dataset2.plot(x = "Time (s)",ax=ax.flatten()[0:5],subplots=True, sharex=False)
fig, ax = plt.subplots(2, 2)
dataset1_sma.plot(x = "Time (s)",ax=ax.flatten()[0:5],subplots=True, sharex=False)
fig, ax = plt.subplots(2, 2)
dataset2_sma.plot(x = "Time (s)",ax=ax.flatten()[0:5],subplots=True, sharex=False)



# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(dataset)
# axs[0, 1].plot(dataset_sma5)
# axs[1, 0].plot(dataset_sma30)
# axs[1, 1].plot(dataset_sma50)
# plt.ylabel('Y')
# plt.xlabel('X')
# plt.plot(dataset)
# plt.plot(dataset_sma5)
# plt.plot(dataset_sma30)
# plt.plot(dataset_sma50)

plt.show()
