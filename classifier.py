import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, roc_curve, RocCurveDisplay, \
    roc_auc_score, f1_score
from sklearn.model_selection import train_test_split, ShuffleSplit, LearningCurveDisplay
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import PreProcessing
import feature_extraction


# test model with 90:10 train/test split
def classify(data, classification):
    X_train, X_test, y_train, y_test = \
        train_test_split(data, classification, test_size=0.1, shuffle=True, random_state=0)

    scaler = StandardScaler()
    l_reg = LogisticRegression(max_iter=10000)

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

    common_params = {
        "X": data,
        "y": classification,
        "train_sizes": np.linspace(0.1, 1.0, 5),
        "cv": ShuffleSplit(n_splits=50, test_size=0.1, random_state=0),
        "score_type": "both",
        "n_jobs": 4,
        "line_kw": {"marker": "o"},
        "std_display_style": "fill_between",
    }

    fig, ax = plt.subplots()
    LearningCurveDisplay.from_estimator(clf, **common_params, ax=ax)
    handles, label = ax.get_legend_handles_labels()
    ax.legend(handles[:2], ["Training Score", "Test Score"])
    ax.set_title(f"Learning Curve for {clf.__class__.__name__}")

    acc = accuracy_score(y_test, y_pred)
    print('accuracy is: ', acc)

    auc = roc_auc_score(y_test, y_clf_prob[:, 1])
    print('the AUC is: ', auc)

    F1 = f1_score(y_test, y_pred)
    print('the F1 score is: ', F1)

    plt.show()


# classify new data from GUI
# uses all train/test data as training data
def classify_input(input_data):
    training_pp = PreProcessing.preprocess()
    training_features = feature_extraction.feature_extraction(training_pp)
    all_training = pd.DataFrame()
    for window in training_features:
        all_training = pd.concat([all_training, window])

    input_pp = PreProcessing.preprocess_input(input_data)
    input_features = feature_extraction.feature_extraction(input_pp)
    all_input = pd.DataFrame()
    for window in input_features:
        all_input = pd.concat([all_input, window])

    # shuffle dataset
    all_training = all_training.sample(frac=1).reset_index(drop=True)

    X_train = all_training.iloc[:, :-1]
    y_train = all_training.iloc[:, -1]

    scaler = StandardScaler()
    l_reg = LogisticRegression(max_iter=10000)

    clf = make_pipeline(scaler, l_reg)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(all_input.drop('Time (s)', axis=1))
    for i in range(len(all_input)):
        all_input['type'] = y_pred
    return all_input


# call this function to test the classifier with 90:10 train/test split
def test():
    dataset = PreProcessing.preprocess()
    dataset_features = feature_extraction.feature_extraction(dataset)
    df = pd.DataFrame()
    for i in dataset_features:
        df = pd.concat([df, i])
    classify(df.iloc[:, :-1], df.loc[:, 'type'].astype('int'))


# test()
