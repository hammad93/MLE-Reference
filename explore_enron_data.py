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

"""
What is the total value of the stock belonging to James Prentice?
"""
print 'James Prentice total stock value: ', enron_data['PRENTICE JAMES']['total_stock_value']
"""
How many email messages do we have from Wesley Colwell to persons of interest?
"""
print "From Wesley to a person of interest: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
"""
Whats the value of stock options exercised by Jeffrey K Skilling?
"""
print "Value of stock options from Skilling: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
"""
Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of total_payments feature)?

How much money did that person get?
"""
print "Total payments from Skilling: ", enron_data['SKILLING JEFFREY K']['total_payments']
print "Total payments from Fastow: ", enron_data['FASTOW ANDREW S']['total_payments']
print "Total payments from Lay: ", enron_data['LAY KENNETH L']['total_payments']
"""
How many folks in this dataset have a quantified salary? What about a known email address?
"""
salaryCount = 0;
emailCount = 0;
for i in enron_data:
    if (enron_data[i]["salary"] != 'NaN'):
        salaryCount+=1
for i in enron_data:
    if (enron_data[i]["email_address"] != 'NaN'):
        emailCount+=1

print "# Quanitified salary: ", salaryCount, " # valid email: ", emailCount

"""
How many people in the E+F dataset (as it currently exists) have NaN for their total payments? What percentage of people in the dataset as a whole is this?
"""
totalPaymentCount = 0
for i in enron_data:
    if (enron_data[i]["total_payments"] == "NaN"):
        totalPaymentCount += 1
print "# NaN for total payments: ", totalPaymentCount, " as percentage: ", ((float(totalPaymentCount) / (len(enron_data.keys()))) * 100), "%"
#note that for the percentage, we convert the type of totalPaymentCount to float to make a float division under Python 2.X
"""
How many POIs in the E+F dataset have NaN for their total payments? What percentage of POIs as a whole is this?
"""
poiPaymentCount = 0
for i in enron_data:
    if (enron_data[i]["poi"] == 1 and enron_data[i]["total_payments"] == "NaN" ):
        poiPaymentCount += 1
print "# POI & NaN for total payments: ", poiPaymentCount, " as percentage: ", ((float(poiPaymentCount) / (len(enron_data.keys()))) * 100), "%"