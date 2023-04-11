import pandas as pd
from matplotlib import pyplot as plt

import data_split


# returns a new DataFrame of extracted features
def extract_features(data):
    window_size = 31
    # need 10+ features total !!!
    features = pd.DataFrame(columns=['maximum', 'minimum', 'range', 'mean', 'median',
                                     'variance', 'skewness', 'standard deviation',
                                     'kurtosis', 'type'])
    # using absolute acceleration column only
    features['maximum'] = data.iloc[:, 4].rolling(window=window_size).max()
    features['minimum'] = data.iloc[:, 4].rolling(window=window_size).min()
    features['range'] = features['maximum'] - features['minimum']
    features['mean'] = data.iloc[:, 4].rolling(window=window_size).mean()
    features['median'] = data.iloc[:, 4].rolling(window=window_size).median()
    features['variance'] = data.iloc[:, 4].rolling(window=window_size).var()
    features['skewness'] = data.iloc[:, 4].rolling(window=window_size).skew()
    features['standard deviation'] = data.iloc[:, 4].rolling(window=window_size).std()
    features['kurtosis'] = data.iloc[:, 4].rolling(window=window_size).kurt()
    features['type'] = data.loc[:, 'type']
    features = features.dropna()
    return features


# for loop to run extract_features iterating through array of 5s window DataFrames
def iterate_extract(data):
    features = []
    for window in data:
        temp = extract_features(window)
        if len(temp.index) > 0:
            features.append(temp)
    return features


def feature_extraction(dataset):
    data_features = iterate_extract(dataset)
    return data_features


# dataset is the array of DataFrames of 5s windows
# feature is the name of the feature to be plotted ('mean', 'range', 'kurtosis', etc.)
def plot_feature_extraction(dataset, feature):
    data_features = iterate_extract(dataset)
    num_data_windows = len(data_features)  # number of 5s windows

    fig, axs = plt.subplots(nrows=num_data_windows, figsize=(20, 10))
    colors = ['red', 'yellow', 'blue', 'green', 'pink', 'purple']
    prev_len = 0
    for i in range(num_data_windows):
        curr_len = len(data_features[i])
        x = [x for x in range(prev_len, prev_len + curr_len)]
        axs[i].plot(x, data_features[i][feature], c=colors[i % 6])
        prev_len = prev_len + curr_len
    plt.show()


# test = data_split.data_split(pd.read_csv('Lucas/WalkingArmsDown.csv'))
# test_features = feature_extraction(test)
