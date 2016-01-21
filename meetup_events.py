import requests
from datetime import datetime, timedelta
import os
import csv
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
meetups = []
for event in events:
  datetime = datetime.fromtimestamp(event['time'] / 1e3)
  # if start < datetime and datetime < end:
  group = str(event['group']['name'])
  name = str(event['name'])
  url = str(event['event_url'])
  start_time = datetime.strftime("%-I:%M")
  meetup = { 'name':name,
             'group':group,
             'datetime':datetime.strftime("%A, %B %-d"),
             'start_time':start_time,
             'url':url }
  meetups.append(meetup)

os.remove('meetups.csv')

with open('meetups.csv', 'w') as csvfile:
  fieldnames = ['name', 'url', 'group', 'datetime', 'start_time']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for meetup in meetups:
    writer.writerow(meetup)
## TODO: Get events from all meetups
## TODO: Filter the meetups down to ones happening this week
## Write the name, group, date, start time, finish time, and url to CSV

