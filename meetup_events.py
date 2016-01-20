import requests
import ipdb

f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()

params = {"sign":"true", "key":api_key, "group_urlname":"bostonpython"}
request = requests.get("http://api.meetup.com/2/events", params)
response = request.json()
events = response['results']

