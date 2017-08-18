import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import pprint


#take user input
consignee_names = raw_input('Enter consignee names separated with comma(,): ')
list_of_consignee_names = map(str, consignee_names.split(''))

print list_of_consignee_names

# list_of_consignee_names.

#if you get list of consignee as input
#convert it to series 
#extract the most recurring pattern from list of consigness and return it as key
series_of_consignee_names = pd.Series(list_of_consignee_names)
print series_of_consignee_names

# pattern = r'.*' + re.escape(list_of_consignee_names[0]) + r'.*'

# pattern = re.compile(r'.*({}).*', re.IGNORECASE)
boom = lambda x:True if any(w in kw for w in x.split()) else False
results = series_of_consignee_names.str.contains(pattern)



# results = series_of_consignee_names.str.contains(pattern)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(dict([('key',list_of_consignee_names[0])]))

print results





# CENSEA INC, CENSEA INC, M/s CENSEA INC., M/S CENSEA INC., CENSEA INC., CENSEA Food Incorporated,BAYFRESH INC, BAY FRESH INC

# ['CENSEA INC,','CENSEA INC','M/s CENSEA INC.,','M/S CENSEA INC.','CENSEA INC.,']

# ['BAYFRESH INC','BAYFRESH INC, 3760 SEATON DR.,','BAYFRESH INC.']







# consignee = pd.read_csv("/home/intrior/projects/trial/consignee.csv", na_values="NA")
# # consignee = pd.read_csv("/home/intrior/projects/trial/consignee.csv", na_values="NA")

# consignee_names_series = consignee['CONSINEE']

# consignee_names_series = consignee_names_series.str.strip()

# # print consignee_names_series

# #create this regex instread of hardcoding it
# # regex_pattern = re.compile(r'.*censea.*', flags=re.IGNORECASE)


# text_to_search = text_to_search.strip()

# # text_to_search = 'india'
# regex_pattern = r".*" + re.escape(text_to_search) + r".*"
# # regex_pattern = r"\w\s" + re.escape(text_to_search) + r"\w"

# results = consignee_names_series[consignee_names_series.str.findall(regex_pattern, flags=re.IGNORECASE).str.len() > 0]
# # results = consignee_names_series.str.findall(r'.*censea.*', flags=re.IGNORECASE)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(dict([(text_to_search,dict([('matches', results.drop_duplicates().values.tolist()), ('total', len(results))]))]))



















# print results
# print len(results)



# sliced_results = results.str.slice()
# print sliced_results

#this what gives results as we want
# y[y.str.findall(r'.*censea.*', flags=re.IGNORECASE).str.len() > 0]


# this works from csv data
# y.str.findall(r'.*censea.*', flags=re.IGNORECASE)

# works for find all
# regex_pat = re.compile(r'.*censea.*', flags=re.IGNORECASE)
# results=y.str.findall(regex_pat)

# gives string s as non list
# slie_series = results.str.slice()


# returns just list of all censea only
# regex_pat = re.compile(r'censea', flags=re.IGNORECASE)

# only beginning with censea
# regex_pat = re.compile(r'^censea', flags=re.IGNORECASE)

