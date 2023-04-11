import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import PreProcessing
import data_split
import feature_extraction


def classify(data, classification):
    X_train, X_test, y_train, y_test = \
        train_test_split(data, classification, test_size=0.1, shuffle=True, random_state=0)

    scaler = StandardScaler()
    l_reg = LogisticRegression(max_iter=10000)

    # pca = PCA(n_components=2)
    # pca_pipe = make_pipeline(scaler, pca)
    # X_train_pca = pca_pipe.fit_transform(X_train)
    # X_test_pca = pca_pipe.fit_transform(X_test)
    # clf = make_pipeline(l_reg)
    # clf.fit(X_train_pca, y_train)
    # y_pred_pca = clf.predict(X_test_pca)
    # acc = accuracy_score(y_test, y_pred_pca)
    # print('accuracy is: ', acc)

    clf = make_pipeline(scaler, l_reg)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_clf_pred = clf.predict_proba(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy: ", acc)


# old test code
# don't use
# preserved as function just in case
def old_test():
    test = []
    walk = data_split.data_split(pd.read_csv('Lucas/WalkingArmsDown.csv'))
    jump = data_split.data_split(pd.read_csv('Lucas/JumpingArmsDown.csv'))
    for window in walk:
        test.append(window)
    for window in jump:
        test.append(window)

    test_class = []

    window_size = 31

    for window in walk:
        if (len(window) - window_size + 1) > 0:
            test_class.append(0)

    for window in jump:
        if (len(window) - window_size + 1) > 0:
            test_class.append(1)

    # walk = 0
    # jump = 1
    print(test_class)

    test_features = feature_extraction.feature_extraction(test)
    print(test_features)

    classify(test_features, test_class)


# walk = data_split.data_split(pd.read_csv('Lucas/WalkingArmsDown.csv'))
# jump = data_split.data_split(pd.read_csv('Lucas/JumpingArmsDown.csv'))
#
# df = pd.DataFrame(columns=['maximum', 'minimum', 'range', 'mean', 'median',
#                                      'variance', 'skewness', 'standard deviation',
#                                      'kurtosis', 'class'])
# walk_features = feature_extraction.feature_extraction(walk)
# jump_features = feature_extraction.feature_extraction(jump)
# for window in walk_features:
#     window['type'] = 0
#     df = pd.concat([df, window])
# for window in jump_features:
#     window['type'] = 1
#     df = pd.concat([df, window])
#
# classify(df.iloc[:, :-1], df.iloc[:, -1].astype('int'))

# df1, df2, df3 = PreProcessing.preprocess()
# print(df1)
# df = pd.concat([df1, df2, df3])
# df = df.dropna()
dataset = PreProcessing.preprocess()
#df = df.dropna()
# print(dataset)
dataset_features = feature_extraction.feature_extraction(dataset)
df = pd.DataFrame()
for i in dataset_features:
    df = pd.concat([df, i])
print(df)
classify(df.iloc[:, :-1], df.loc[:, 'type'].astype('int'))
