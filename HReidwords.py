import requests
import csv
import pprint
from nltk.corpus import stopwords

query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
		   		 'entity_type': 'legislator',
		   		 'entity_value': 'r000146',
                         'sort': 'count desc'
                         }

endpoint = 'http://capitolwords.org/api/phrases.json'
response = requests.get(endpoint, params=query_params).json()

with open("HReid_words.csv", "w") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['word', 'count'])

	for n in response:
         if n['ngram'] not in stopwords.words('english'):
             word = n['ngram']
             count = n['count']
             writer.writerow([word, count])