# -*- coding: utf-8 -*-
"""data_2_check_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G1a4p3-9XTuJh_ZpfYAYP2dxKpXDLmFI

**Your Instructions:**

*To complete the first knowledge check, do the following:*

* Create a GitHub repo called "data_1_checks". You will upload ALL knowledge checks to this repo in the future.

* Send that link to your mentor so they can check it when you finish the assignment.

* Make a .py (or .ipynb) file that contains the following (your choice of editor does not matter!) and do the following:

* Pull in data from an API. Here's a list of public APIs that don't require Auth keys, though if you have another API you want to use feel free: https://apipheny.io/free-api/

* Find and print TWO descriptive statistics about your data. This can be absolutely anything, from the mean() or sum() of a column to the number of different categories, to the number of null values in a column. We just want to see two pieces of information.

* Write a query in Pandas to select a particular set of your data. You can use a mask or with .query(), but we want you to pull out a subset based on any parameter you like. This could be "show me every row where HTTPS=False" or anything else.

* Select and print the SECOND AND THIRD columns of your data frame.

* Select and print the FIRST 4 rows of you data frame.

* Commit your changes.

- Push your changes to your repo and notify your mentor!
"""

#Duane Hellums, Code Louisville, 11:20 AM, 5/19/22

import requests
import json
import pandas as pd

r = requests.get('https://deperu.com/api/rest/noticias.json') #download Spanish language news items from the country of Peru

json_data = json.loads(r.text) #grab the json data from the page response

print(json_data) #print out the json data to eyeball validate download and conversion

df = pd.DataFrame(data=json_data) #load the json data into a pandas dataframe

df.head(3) #let's see the 3 most recent news items (at the top of the dataframe)

df.info() #number of records, columns, non-nulls, and data type

df.describe() #some additional data about the deta set

df.shape[1] #total number of columns

df.shape[0] #total number of rows or records

df[df.palsclave.str.contains('Ucrania')].shape[0] #total number of news items about Ukraine

df['resumen'].isna().sum() #total number of NULL records in news items

df[df.palsclave.str.contains('gas')] #show any new items about gas

print(df[df.palsclave.str.contains('gas')]) #details on the gas news items in Peru

print(df[df.palsclave.str.contains('gas')].iloc[0,0]) #let's see the scalar/full title slug

print(df[df.palsclave.str.contains('gas')].iloc[0,1]) #let's see the scalar/full news item

print(df[df.palsclave.str.contains('gas')].iloc[0,5]) #let's see the scalar/full link so we can click on it

df[['resumen', 'palsclave']] #select and print columns 2 and 3

df.head(4) #select and print the first four rows

print("Don't have a good day.\nHave a great day!")