import requests
from datetime import datetime, timedelta
import ipdb

f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()
present = datetime.now()
start = present - timedelta(days=present.weekday())
end = start + timedelta(days=4)

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
datetime = datetime.fromtimestamp(events[0]['time'] / 1e3)
meetups = []
if start < datetime and datetime < end:
  group = events[0]['group']['name']
  name = events[0]['name']
  url = events[0]['event_url']
  duration = events[0]['duration'] / 1e3
  start_time = datetime.strftime("%-I:%M")
  ipdb.set_trace()
  meetup = { 'name':name,
             'group':group,
             'datetime':datetime.strftime("%A, %B %-d"),
             'start_time':0,
             'finish_time':1,
             'url':url }
  meetups.append(meetup)

## TODO: Get events from all meetups
## TODO: Filter the meetups down to ones happening this week
## Write the name, group, date, start time, finish time, and url to CSV

