import requests
import ipdb

f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()

meetups = ['bostonpython',
           'Maptime-Boston', 
           'ACM-Boston',
           'Cambridge-Hackspace',
           'Boston-Data-Mining',
           'SocialDataBoston',
           'Boston-Digital-Analytics-Meetup',
           'BigDataBoston',
           'Boston-Algorithmic-Trading',
           'The-Data-Scientist',
           'Big-Data-Developers-in-Boston',
           'PyData-Boston',
           'BigDBN',
           'graphdb-boston',
           'FREE-Big-Data-Hands-On-Workshops',
           'julia-cajun',
           'The-Boston-Cassandra-Users',
           'Happy-Data-Hour-Boston'
           ]
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

