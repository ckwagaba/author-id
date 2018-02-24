#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# import SVC
from sklearn.svm import SVC

# create classifier
clf = SVC(kernel='linear')

# train the classifier
clf.fit(features_train, labels_train)

# make predictions
pred = clf.predict(features_test)
print pred

# import accuracy score
from sklearn.metrics import accuracy_score

# calculate effeciency
score = accuracy_score(labels_test, pred)
print score
