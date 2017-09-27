# Dependencies
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


# Set the seed (reproducibility)
random.seed(0)


# Data import and cleaning
df1 = pd.read_csv("./speedbumps_1.csv")  # read data from the .csv file
df2 = pd.read_csv("./speedbumps_2.csv")  # read data from the .csv file
df3 = pd.read_csv("./speedbumps_3.csv")  # read data from the .csv file
df4 = pd.read_csv("./speedbumps_4.csv")  # read data from the .csv file
df = pd.read_csv("./speedbumps_5.csv")  # read data from the .csv file
df1 = df1.loc[:, ('speedbump', 'Speed', 'X', 'Y', 'Z', 'z_jolt')]  # only select relevant columns
df2 = df2.loc[:, ('speedbump', 'Speed', 'X', 'Y', 'Z', 'z_jolt')]  # only select relevant columns
df3 = df3.loc[:, ('speedbump', 'Speed', 'X', 'Y', 'Z', 'z_jolt')]  # only select relevant columns
df4 = df4.loc[:, ('speedbump', 'Speed', 'X', 'Y', 'Z', 'z_jolt')]  # only select relevant columns
df = df.loc[:, ('speedbump', 'Speed', 'X', 'Y', 'Z', 'z_jolt')]  # only select relevant columns
keywords = ['yes', 'no']
mapping = [1, 0]
df1 = df1.replace(keywords, mapping)
df2 = df2.replace(keywords, mapping)
df3 = df3.replace(keywords, mapping)
df4 = df4.replace(keywords, mapping)
df = df.replace(keywords, mapping)
df = df.append(df1)
df = df.append(df2)
df = df.append(df3)
df = df.append(df4)


# Decision Tree Model 1
# Separate Y and X variables
df_label = df.loc[:, 'speedbump']
df_feature = df.loc[:, ('Speed', 'X', 'Y', 'Z', 'z_jolt')]
Y = df_label.as_matrix()
X = df_feature.as_matrix()


# Prepare for cross-validation
clf = DecisionTreeClassifier()  # create a DecisionTreeClassifier
f1_sum = 0.00  # sum of F1 scores
cv = 100;  # number of cross-validations


# Start cross-validation
for i in range(0, cv, 1):

    # split to train and test sets
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, shuffle=True)

    # start training
    clf = clf.fit(train_X, train_Y)  # fit the training data

    # start testing
    predicted_Y = clf.predict(test_X)  # predict on the testing data

    # calculate the F1 score
    f1 = metrics.f1_score(test_Y, predicted_Y, average='binary')  # calculate the F1 score
    f1_sum += f1

    # calculate the confusion matrix
    matrix = metrics.confusion_matrix(test_Y, predicted_Y)

    # print iterative result
    # print('\n-----------------------------------')
    # print('Iteration ', i)
    # print('Features: speed, X-accel, Y-accel, Z-accel, Z-jolt')
    # print('Labels: speedbump (1 = yes, 0 = no)')
    # print('F1 score:', f1)
    # print(matrix)


# Calculate cross-validation average
f1_average = f1_sum / cv
print('\n-----------------------------------')
print('sklearn Decision Tree Model 1')
print('\tFeatures: speed, X-accel, Y-accel, Z-accel, Z-jolt')
print('\tLabels: speedbump (1 = yes, 0 = no)')
print('\tAverage F1 score:', f1_average)


# Decision Tree Model 2
# Separate Y and X variables
df_label = df.loc[:, 'speedbump']
df_feature = df.loc[:, ('Speed', 'X', 'Y', 'Z')]
Y = df_label.as_matrix()
X = df_feature.as_matrix()


# Prepare for cross-validation
clf = DecisionTreeClassifier()  # create a DecisionTreeClassifier
f1_sum = 0.00  # sum of F1 scores
cv = 100;  # number of cross-validations


# Start cross-validation
for i in range(0, cv, 1):

    # split to train and test sets
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, shuffle=True)

    # start training
    clf = clf.fit(train_X, train_Y)  # fit the training data

    # start testing
    predicted_Y = clf.predict(test_X)  # predict on the testing data

    # calculate the F1 score
    f1 = metrics.f1_score(test_Y, predicted_Y, average='binary')  # calculate the F1 score
    f1_sum += f1

    # calculate the confusion matrix
    matrix = metrics.confusion_matrix(test_Y, predicted_Y)

    # print iterative result
    # print('\n-----------------------------------')
    # print('Iteration ', i)
    # print('Features: speed, X-accel, Y-accel, Z-accel')
    # print('Labels: speedbump (1 = yes, 0 = no)')
    # print('F1 score:', f1)
    # print(matrix)


# Calculate cross-validation average
f1_average = f1_sum / cv
print('\n-----------------------------------')
print('sklearn Decision Tree Model 2')
print('\tFeatures: speed, X-accel, Y-accel, Z-accel')
print('\tLabels: speedbump (1 = yes, 0 = no)')
print('\tAverage F1 score:', f1_average)


# Decision Tree Model 3
# Separate Y and X variables
df_label = df.loc[:, 'speedbump']
df_feature = df.loc[:, ('Speed', 'X', 'Y', 'z_jolt')]
Y = df_label.as_matrix()
X = df_feature.as_matrix()


# Prepare for cross-validation
clf = DecisionTreeClassifier()  # create a DecisionTreeClassifier
f1_sum = 0.00  # sum of F1 scores
cv = 100;  # number of cross-validations


# Start cross-validation
for i in range(0, cv, 1):

    # split to train and test sets
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, shuffle=True)

    # start training
    clf = clf.fit(train_X, train_Y)  # fit the training data

    # start testing
    predicted_Y = clf.predict(test_X)  # predict on the testing data

    # calculate the F1 score
    f1 = metrics.f1_score(test_Y, predicted_Y, average='binary')  # calculate the F1 score
    f1_sum += f1

    # calculate the confusion matrix
    matrix = metrics.confusion_matrix(test_Y, predicted_Y)

    # print iterative result
    # print('\n-----------------------------------')
    # print('Iteration ', i)
    # print('Features: speed, X-accel, Y-accel, Z-jolt')
    # print('Labels: speedbump (1 = yes, 0 = no)')
    # print('F1 score:', f1)
    # print(matrix)


# Calculate cross-validation average
f1_average = f1_sum / cv
print('\n-----------------------------------')
print('sklearn Decision Tree Model 3')
print('\tFeatures: speed, X-accel, Y-accel, Z-jolt')
print('\tLabels: speedbump (1 = yes, 0 = no)')
print('\tAverage F1 score:', f1_average)
