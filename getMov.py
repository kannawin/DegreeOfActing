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

values = []
values.append('api_key')
values.append('year')
values.append('include_adult')
values.append('query')
values.append('language')


queryString = urllib.urlencode(pairs)

cheatURL = 'https://api.themoviedb.org/3/search/movie?api_key=97e4335bd73002b6731fc902f3748e96&language=en-US&query=The%20Shawshank%20Redemption&page=1&include_adult=false&year=1995'

url = 'https://api.themoviedb.org/3/search/movie?'
url += queryString

r = requests.get(url)
print r.status_code
print r.content

##print url


