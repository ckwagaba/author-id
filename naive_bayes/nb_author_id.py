#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
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

# inspecting the values
# print "features_train: ", features_train
# print "features_test: ", features_test
# print "labels_train: ", labels_train
# print "labels_test: ", labels_test

# import GaussianNB
from sklearn.naive_bayes import GaussianNB

# import accuracy calculator
from sklearn.metrics import accuracy_score

clf = GaussianNB()

# training start time
training_start_time = time()

# training
clf.fit(features_train, labels_train)

# training time in seconds
print "Training time: ", round(time() - training_start_time, 3), "s"

# prediction start time
prediction_start_time = time()

# testing: making predictions
pred = clf.predict(features_test)

# prediction time in seconds
print "Prediction time: ", round(time() - prediction_start_time, 3), "s"

# prediction
print pred

# accuracy
score = accuracy_score(labels_test, pred)
print score
