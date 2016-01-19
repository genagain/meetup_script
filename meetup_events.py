import requests

f = open('api_key.txt','r')
api_key = f.read()
api_key = api_key.rstrip()
print(api_key)
