#!/usr/bin/python

# Import necessary modules
import requests
import json
import random

# Define credentials for Oxford Dictionary API
baseUrl = "https://od-api.oxforddictionaries.com/api/v1"
appId = ""
appKey = ""

# Define query parameters
lang = "en"
method = "wordlist"
filter = "lexicalCategory"

# Define structure of name
pattern = ["adjective", "noun", "verb", "noun"]
names = []

print ("Generating your custom RPG Name...")

# Loop through pattern and make call to API
for i in range(len(pattern)):
  offset = str(random.randint(1,20000))
  url = baseUrl + "/" + method + "/" + lang + "/" + filter + "=" + pattern[i] + "?limit=1&offset=" + offset
  req = requests.get(url, headers = {'app_id': appId, 'app_key': appKey})
  json_str = json.dumps(req.json())
  res = json.loads(json_str)
  names.append(res['results'][0]['word'])

# If names[2] ends in 'e', let's strip it off
if names[2][-1:] == 'e':
  names[2] = names[2][:end]

# Join all the parts into a coherent string
name = ("The " + names[0] + " " + names[1] + " of " + names[2] + "ing " + names[3])

# Output the name
print("Your name is: ")
print(name)

