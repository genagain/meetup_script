import requests
from datetime import datetime, timedelta, date
import os
import csv
import ipdb

#opening, reading and cleaning api key
f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()

#deducing Monday and Friday of this week
present = datetime.now()
start = present - timedelta(days=present.weekday())
end = start + timedelta(days=4)

all_meetups = ['bostonpython',
           'Maptime-Boston', 
           'ACM-Boston',
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
           'bostonml',
           'Boston-Sports-Analytics-Meetup',
           'Cambridge-Dataflow-Analytics-Meetup',
           'Happy-Data-Hour-Boston']
meetups = []

#Getting all of the meetup events
for meetup in all_meetups:
  params = {"sign":"true", "key":api_key, "group_urlname":meetup}
  request = requests.get("http://api.meetup.com/2/events", params)
  response = request.json()
  events = response['results']

  for event in events:
    datetime = datetime.fromtimestamp(event['time'] / 1e3)

    #Checking to see if the event is happening this week
    if start < datetime and datetime < end:

      #Parsing the event data
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

#Writing all the meetups happening this week to a CSV
with open('meetups.csv', 'w') as csvfile:
  fieldnames = ['name', 'url', 'group', 'datetime', 'start_time']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for meetup in meetups:
    writer.writerow(meetup)

