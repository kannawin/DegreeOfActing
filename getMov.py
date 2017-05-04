#!/usr/bin/python
import requests
import json
import urllib
import httplib


year = 1995
search = 'The Shawshank Redemption'
api = '97e4335bd73002b6731fc902f3748e96'

pairs = {
	'api_key' : api,
	"year" : "1995",
	"include_adult":"false",
	"query" : search,
	"language" : "en-US",
}

queryString = urllib.urlencode(pairs)


url = 'https://api.themoviedb.org/3/search/movie?'
url += queryString

r = requests.get(url)
print r.status_code
result = json.loads(r.content)

print result['results'][0]['title']


