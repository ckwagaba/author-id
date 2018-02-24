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

# training start time
training_start_time = time()

# train the classifier
clf.fit(features_train, labels_train)

# training time in seconds
print "Training time: ", round(time() - training_start_time, 3), "s"

# prediction start time
prediction_start_time = time()

# make predictions
pred = clf.predict(features_test)

# prediction time in seconds
print "Prediction time: ", round(time() - prediction_start_time, 3), "s"

# prediction
print pred

# import accuracy score
from sklearn.metrics import accuracy_score

# calculate effeciency
score = accuracy_score(labels_test, pred)
print score
