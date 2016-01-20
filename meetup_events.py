import requests
import ipdb

f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()

meetups = ['bostonpython']
params = {"sign":"true", "key":api_key, "group_urlname":"bostonpython"}
request = requests.get("http://api.meetup.com/2/events", params)
response = request.json()
events = response['results']
datetime = datetime.datetime.fromtimestamp(events[0]['time'] / 1e3)
group = events[0]['group']['name']
name = events[0]['name']

## TODO: Get events from all meetups
## TODO: Filter the meetups down to ones happening this week
## Write the name, group, time, duration, and url to CSV

