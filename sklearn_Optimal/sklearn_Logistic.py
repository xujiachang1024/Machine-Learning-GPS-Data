# Dependencies
import random
import pandas as pd
import numpy as np
import warnings
from scipy import stats
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.decomposition import PCA
from sklearn import metrics


# Set the seed (reproducibility)
random.seed(0)
warnings.filterwarnings('ignore', category=UndefinedMetricWarning)


# Data import and cleaning
df = pd.read_csv("./kenya_oct_15_data_labeled.csv")  # read data from the .csv file


# Decision Tree Model 1
# Separate Y and X variables
df_label = df.loc[:, 'speedbump']
df_feature = df.loc[:, ('x', 'z')]

numPoints = 4;
feature1 = "x"
feature2 = "z"
feature3 = ""
feature4 = ""
feature5 = ""
feature6 = ""

for i in range(1,numPoints+1):
    if feature1 != "":
        new_feature = (feature1, i)
        df_feature[new_feature] = df_feature[feature1].shift(i)
    if feature2 != "":
        new_feature = (feature2, i)
        df_feature[new_feature] = df_feature[feature2].shift(i)
    if feature3 != "":
        new_feature = (feature3, i)
        df_feature[new_feature] = df_feature[feature3].shift(i)
    if feature4 != "":
        new_feature = (feature4, i)
        df_feature[new_feature] = df_feature[feature4].shift(i)
    if feature5 != "":
        new_feature = (feature5, i)
        df_feature[new_feature] = df_feature[feature5].shift(i)
    if feature6 != "":
        new_feature = (feature6, i)
        df_feature[new_feature] = df_feature[feature6].shift(i)

df_feature = df_feature[numPoints:]
df_label = df_label[numPoints:]
df_feature.index = range(len(df_feature))
df_label.index = range(len(df_label))

Y = df_label.as_matrix()
X = df_feature.as_matrix()


# Dimensionality reduction
a_normalized = preprocessing.normalize(preprocessing.scale(X), norm='l2')
# etc_model = ExtraTreesClassifier()
# etc_model.fit(a_normalized, Y)
# print('Feature Importance:')
# print(etc_model.feature_importances_)
# pca = PCA(n_components=2)
# a_pca = pca.fit_transform(a_normalized)


# Prepare for cross-validation
clf = LogisticRegression(penalty='l2', tol=1e-3, C=1000, max_iter=1000)
f1_scores = []  # sum of F1 scores
cv = 10  # number of cross-validations


# Start cross-validation
for i in range(0, cv, 1):

    # split to train and test sets
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, shuffle=True)

    # start training
    clf = clf.fit(train_X, train_Y)  # fit the training data

    # start testing
    predicted_Y = clf.predict(test_X)  # predict on the testing data

    # calculate precision
    precision = metrics.precision_score(test_Y, predicted_Y, average='binary', pos_label=1)
    precision = float(precision)

    # calculate recall
    recall = metrics.recall_score(test_Y, predicted_Y, average='binary', pos_label=1)
    recall = float(recall)

    # calculate F1 score
    if (precision + recall) != 0:
        f1 = (2 * precision * recall) / (precision + recall)
        f1_scores.append(f1)


# Calculate cross-validation average
print('\n-----------------------------------')
print('sklearn.linear_model.LogisticRegression Model 1')
print('\tFeatures: speed, X-accel, Y-accel, Z-accel, Z-jolt')
print('\tLabels: speedbump (1 = yes, 0 = no)')
print('\tAverage F1 score:', np.mean(f1_scores))
print('\tStdDev F1 score:', np.std(f1_scores))
print('\tMedian F1 score:', np.median(f1_scores))
print('\tIQR F1 score:', stats.iqr(f1_scores))
print('\tSkewness F1 score:', stats.skew(f1_scores))


# # Logistic Regression Model 2
# # Separate Y and X variables
# df_label = df.loc[:, 'speedbump']
# df_feature = df.loc[:, ('Speed', 'Z', 'z_jolt')]
# Y = df_label.as_matrix()
# X = df_feature.as_matrix()
#
#
# # # Dimensionality reduction
# a_normalized = preprocessing.normalize(preprocessing.scale(X), norm='l2')
# # etc_model = ExtraTreesClassifier()
# # etc_model.fit(a_normalized, Y)
# # print('Feature Importance:')
# # print(etc_model.feature_importances_)
# # pca = PCA(n_components=0)
# # a_pca = pca.fit_transform(a_normalized)
#
#
# # Prepare for cross-validation
# clf = LogisticRegression(penalty='l2', tol=1e-3, C=1000, max_iter=1000)
# f1_scores = []  # sum of F1 scores
# cv = 10  # number of cross-validations
#
#
# # Start cross-validation
# for i in range(0, cv, 1):
#
#     # split to train and test sets
#     train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, shuffle=True)
#
#     # start training
#     clf = clf.fit(train_X, train_Y)  # fit the training data
#
#     # start testing
#     predicted_Y = clf.predict(test_X)  # predict on the testing data
#
#     # calculate precision
#     precision = metrics.precision_score(test_Y, predicted_Y, average='binary', pos_label=1)
#     precision = float(precision)
#
#     # calculate recall
#     recall = metrics.recall_score(test_Y, predicted_Y, average='binary', pos_label=1)
#     recall = float(recall)
#
#     # calculate F1 score
#     if (precision + recall) != 0:
#         f1 = (2 * precision * recall) / (precision + recall)
#         f1_scores.append(f1)
#
#
# # Calculate cross-validation average
# print('\n-----------------------------------')
# print('sklearn.linear_model.LogisticRegression Model 2')
# print('\tFeatures: speed, Z-accel, Z-jolt')
# print('\tLabels: speedbump (1 = yes, 0 = no)')
# print('\tAverage F1 score:', np.mean(f1_scores))
# print('\tStdDev F1 score:', np.std(f1_scores))
# print('\tMedian F1 score:', np.median(f1_scores))
# print('\tIQR F1 score:', stats.iqr(f1_scores))
# print('\tSkewness F1 score:', stats.skew(f1_scores))
#
