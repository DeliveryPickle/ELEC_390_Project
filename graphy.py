import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Raw Data.csv")
data = dataset.iloc[:, 1:5]
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
data.plot(ax=ax.flatten()[0:4], subplots=True, sharex=False)
fig.tight_layout()
plt.show()