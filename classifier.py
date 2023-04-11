import pandas as pd
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, roc_curve, RocCurveDisplay, \
    roc_auc_score, f1_score
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
    y_clf_prob = clf.predict_proba(X_test)
    print('y_pred is: ', y_pred)
    print('y_clf_prob is: ', y_clf_prob)

    cm = confusion_matrix(y_test, y_pred)
    cm_display = ConfusionMatrixDisplay(cm).plot()

    fpr, tpr, _ = roc_curve(y_test, y_clf_prob[:, 1], pos_label=clf.classes_[1])
    roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()

    acc = accuracy_score(y_test, y_pred)
    print('accuracy is: ', acc)

    auc = roc_auc_score(y_test, y_clf_prob[:, 1])
    print('the AUC is: ', auc)

    F1 = f1_score(y_test, y_pred)
    print('the F1 score is: ', F1)

    plt.show()


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


dataset = PreProcessing.preprocess()
dataset_features = feature_extraction.feature_extraction(dataset)
df = pd.DataFrame()
for i in dataset_features:
    df = pd.concat([df, i])
classify(df.iloc[:, :-1], df.loc[:, 'type'].astype('int'))
