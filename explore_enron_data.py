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

import pickle
"""
pickle will make the object of type dict (dictionary)
we will then have a dictionary of a dictionary

"""
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "number of people: ", len(enron_data.keys())
print "number of attributes per person: ", len(enron_data["SKILLING JEFFREY K"])

"""
The poi feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
1) Iterate through all items in the dictionary
2) Access the "poi" feature and add to count if true (or 1)
data[person_name]["poi"]==1
"""
count = 0
for i in enron_data:
    if enron_data[i]["poi"] == 1 :
        count+=1
print "number of poi's: ", count