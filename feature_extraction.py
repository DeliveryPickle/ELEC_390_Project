import pandas as pd
from matplotlib import pyplot as plt

# should use 5s windows
dataset = pd.read_csv('Lucas/JumpingArmsDown.csv')

# need 10+ features total
#features = pd.DataFrame(columns=['maximum', 'minimum', 'range', 'mean', 'median', 'variance', 'skewness'])
features = pd.DataFrame(columns=['maximum', 'minimum', 'mean', 'median', 'variance', 'skewness', 'standard deviation'])
window_size = 100
# using absolute acceleration column only
features['maximum'] = dataset.iloc[:, 4].rolling(window=window_size).max()
features['minimum'] = dataset.iloc[:, 4].rolling(window=window_size).min()
#features['range'] = dataset.iloc[:, 4].rolling(window=window_size).range() # this is not a function/there is no range function?
                                                                            # might need to take difference of max and min columns to get range?
features['mean'] = dataset.iloc[:, 4].rolling(window=window_size).mean()
features['median'] = dataset.iloc[:, 4].rolling(window=window_size).median()
features['variance'] = dataset.iloc[:, 4].rolling(window=window_size).var()
features['skewness'] = dataset.iloc[:, 4].rolling(window=window_size).skew()
features['standard deviation'] = dataset.iloc[:, 4].rolling(window=window_size).std()
features = features.dropna()
print(features)

fig, ax = plt.subplots(figsize=(10, 10))
x = [x for x in range(features['maximum'].size)]
ax.plot(x, features['standard deviation'])
ax.set_xlabel('Number of the Window')
ax.set_ylabel('Value of the std')
plt.show()
