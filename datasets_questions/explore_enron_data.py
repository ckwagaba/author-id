#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

# import pickle
#
# enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#
# poi = 0
#
# for p in enron_data:
#     if enron_data[p]["poi"] == 1:
#         poi += 1
#
# print poi

with open("../final_project/poi_names.txt") as f:
    data = f.readlines()

# for n, line in enumerate(data, 1):
#     print '{:2}.'.format(n), line.rstrip()

print len(data) - 2
