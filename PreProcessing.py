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

# Preprocessing
filePath = ["WalkingFrontPocket.csv", "WalkingBackPocket.csv", "WalkingCoatPocket.csv", "WalkingArmsUp.csv", "WalkingArmsDown.csv", "JumpingFrontPocket.csv", "JumpingBackPocket.csv", "JumpingCoatPocket.csv", "JumpingArmsUp.csv", "JumpingArmsDown.csv"]
Elise_matrix = {}
Simon_matrix = {}
Lucas_matrix = {}

window_size = 57

for i in filePath:
    Elise_matrix = pd.read_csv("Elise/" + i)
    temp = data_split(Elise_matrix)
    for j in range(len(temp)):
        data = temp[j]
        if len(data) > window_size:
            # fig, ax = plt.subplots(2, 2)
            # data.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Elise' + str(i) + ' (Unfiltered)', fontsize=12)

            # Moving Average Filter
            Elise_data_sma = data.rolling(window_size).mean()
            # fig, ax = plt.subplots(2, 2)
            # Elise_data_sma.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Elise' + str(i) + ' (SMA 71)', fontsize=12)

            # Normalization
            Elise_data_normalized = Elise_data_sma.copy()
            Elise_data_normalized = (Elise_data_normalized - Elise_data_normalized.min()) / (Elise_data_normalized.max() - Elise_data_normalized.min())
            # fig, ax = plt.subplots(2, 2)
            # Elise_data_normalized.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Normalized Elise ' + str(i) + ' (SMA 71)', fontsize=12)
            # plt.show()

for i in filePath:
    Simon_matrix = pd.read_csv("Simon/" + i)
    temp = data_split(Simon_matrix)
    for j in range(len(temp)):
        data = temp[j]
        if len(data) > window_size:
            # fig, ax = plt.subplots(2, 2)
            # data.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Simon' + str(i) + ' (Unfiltered)', fontsize=12)

            # Moving Average Filter
            Simon_data_sma = data.rolling(window_size).mean()
            # fig, ax = plt.subplots(2, 2)
            # Simon_data_sma.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Simon' + str(i) + ' (SMA 71)', fontsize=12)

            # Normalization
            Simon_data_normalized = Simon_data_sma.copy()
            Simon_data_normalized = (Simon_data_normalized - Simon_data_normalized.min()) / (Simon_data_normalized.max() - Simon_data_normalized.min())
            # fig, ax = plt.subplots(2, 2)
            # Simon_data_normalized.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Normalized Simon ' + str(i) + ' (SMA 71)', fontsize=12)
            # plt.show()

for i in filePath:
    Lucas_matrix = pd.read_csv("Lucas/" + i)
    temp = data_split(Lucas_matrix)
    for j in range(len(temp)):
        data = temp[j]
        if len(data) > window_size:
            # fig, ax = plt.subplots(2, 2)
            # data.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Lucas' + str(i) + ' (Unfiltered)', fontsize=12)

            # Moving Average Filter
            Lucas_data_sma = data.rolling(window_size).mean()
            # fig, ax = plt.subplots(2, 2)
            # Lucas_data_sma.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            # fig.suptitle('Lucas' + str(i) + ' (SMA 71)', fontsize=12)

            # Normalization
            Lucas_data_normalized = Lucas_data_sma.copy()
            Lucas_data_normalized = (Lucas_data_normalized - Lucas_data_normalized.min()) / (Lucas_data_normalized.max() - Lucas_data_normalized.min())
            fig, ax = plt.subplots(2, 2)
            Lucas_data_normalized.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False)
            fig.suptitle('Normalized Lucas ' + str(i) + ' (SMA 71)', fontsize=12)
            plt.show()

