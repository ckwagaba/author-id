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

# create classifier: C gotta be uppercase
clf = SVC(kernel='rbf', C=10000)

# training start time
training_start_time = time()

# slice the training dataset down
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

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

# class of 10th
print pred[10]

# class of 26th
print pred[26]

# class of 50th
print pred[50]

# Chris (1) emails predicted
chris_emails = []

for event in pred:
    if event == 1:
        chris_emails.append(event)

print len(chris_emails)

# import accuracy score
from sklearn.metrics import accuracy_score

# calculate effeciency
score = accuracy_score(labels_test, pred)
print score
