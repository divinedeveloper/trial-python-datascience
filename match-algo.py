import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import pprint


consignee = pd.read_csv("/home/intrior/projects/trial/consignee.csv", na_values="NA")
# consignee = pd.read_csv("/home/intrior/projects/trial/consignee.csv", na_values="NA")

consignee_names_series = consignee['CONSINEE']

consignee_names_series = consignee_names_series.str.strip()

# print consignee_names_series

#create this regex instread of hardcoding it
# regex_pattern = re.compile(r'.*censea.*', flags=re.IGNORECASE)

#take user input
text_to_search = raw_input('Enter consignee name to search: ')

text_to_search = text_to_search.strip()

# text_to_search = 'india'
# regex_pattern = r".*" + re.escape(text_to_search) + r".*"
regex_pattern = r".* ?" + re.escape(text_to_search) + r".*"

results = consignee_names_series[consignee_names_series.str.findall(regex_pattern, flags=re.IGNORECASE).str.len() > 0]
# results = consignee_names_series.str.findall(r'.*censea.*', flags=re.IGNORECASE)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dict([(text_to_search,dict([('matches', results.drop_duplicates().values.tolist()), ('total', len(results))]))]))





#if you get list of consignee as input
#convert it to series 
#extract the most recurring pattern from list of consigness and return it as key









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

