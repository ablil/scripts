#!/usr/bin/env python3

from twython import Twython
import json

# read Twitter creds from file
creds = {}
with open('twitter_creds.json') as json_data:
    creds = json.load(json_data)

twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

followers = twitter.get_followers_ids()
print(followers['ids'])