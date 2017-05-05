#!/usr/bin/python
import requests
import json
import urllib
import httplib


year = 1995
search = 'The Shawshank Redemption'
api = '97e4335bd73002b6731fc902f3748e96'


for m in range(1,4000):
	pairs = {
		'api_key' : api,
		"language" : "en-US",
	}

	queryString = urllib.urlencode(pairs)


	url = 'https://api.themoviedb.org/3/person/'+str(m)+'/combined_credits?'
	url += queryString
	
	r = requests.get(url)
	if(r.status_code == 200):
		result = json.loads(r.content)

		films = []
		media = []
		job = []

		for i in result['cast']:
			films.append(i['id'])
			media.append(i['media_type'])

		print len(films)

	
