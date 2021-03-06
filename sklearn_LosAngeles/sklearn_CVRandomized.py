# Dependencies
import random
import pandas as pd
import numpy as np
import warnings
from time import time
from scipy import stats
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV


# Set the seed (reproducibility)
random.seed(0)
warnings.filterwarnings('ignore', category=UndefinedMetricWarning)


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
df = df.append(df1)
df = df.append(df2)
df = df.append(df3)
df = df.append(df4)
keywords = ['yes', 'no']
mapping = [1, 0]
df = df.replace(keywords, mapping)

DT_CONST = 0
RFC_CONST = 1
GB_CONST = 2
MLP_CONST = 3
LOG_CONST = 4


MODEL = 2


# Separate Y and X variables
df_label = df.loc[:, 'speedbump']
df_feature = df.loc[:, ('Speed', 'X', 'Y', 'Z', 'z_jolt')]
Y = df_label.as_matrix()
X = df_feature.as_matrix()


# Create a DecisionTreeClassifier
if(MODEL == DT_CONST):
    clf = DecisionTreeClassifier(random_state=0)

    # Specify parameters and distributions to sample from
    param_dist = {"criterion": ["gini", "entropy"],
                  "splitter": ["best", "random"],
                  "max_depth": [5, 4, 3, 2, 1, None],
                  "min_samples_split": [2, 3, 10],
                  "min_samples_leaf": [1, 3, 10],
                  "max_features": ["auto", "log2", None]}

elif(MODEL == RFC_CONST):
    clf = clf = RandomForestClassifier(random_state=0)

    # Specify parameters and distributions to sample from
    param_dist = {"criterion": ["gini", "entropy"],
                  "n_estimators": [9,10,11],
                  "max_depth": [5, 4, 3, 2, 1, None],
                  "min_samples_split": [2, 3, 10],
                  "min_samples_leaf": [1, 3, 10],
                  "max_features": ["auto", "log2", None]}


elif(MODEL == GB_CONST):
    clf = GradientBoostingClassifier(random_state=0)  # create a GradientBoostingClassifier

    # Specify parameters and distributions to sample from
    param_dist = {"learning_rate": [.01, .1, 1],
                  "n_estimators": [100, 150, 200],
                  "max_depth": [10, 5, 3, None],
                  "min_samples_split": [2, 6, 10],
                  "min_samples_leaf": [1, 6, 10],
                  "max_features": [3, 4, None]}

elif(MODEL == MLP_CONST):
    clf = MLPClassifier(random_state=0)

    # Specify parameters and distributions to sample from
    param_dist = {"solver": ['lbfgs', 'sgd', 'adam'],
                  "hidden_layer_sizes": [(5,2), (7,3), (10,2), (100) ],
                  'learning_rate':['constant', 'invscaling', 'adaptive']}

elif(MODEL == LOG_CONST):
    clf = LogisticRegression(penalty='l2')

    # Specify parameters and distributions to sample from
    param_dist = {"solver": ['newton-cg', 'lbfgs', 'sag'],
                  "max_iter": [100, 1000, 2000],
                  'multi_class': ['ovr', 'multinomial']}





# Utility function to report best scores
def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Hyper-parameters: {0}".format(results['params'][candidate]))
            print("")



# Run randomized search
n_iter_search = 50
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, cv=10, n_iter=n_iter_search, scoring='f1')
start = time()
random_search.fit(X, Y)
print("RandomizedSearchCV took %.2f seconds for %d candidates parameter settings." % ((time() - start), n_iter_search))
print(" ")
report(random_search.cv_results_)
