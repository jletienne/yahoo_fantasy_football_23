league_id = '1077375'

import pandas as pd
from yahoo_oauth import OAuth2
import logging
import json
from json import dumps
import datetime
import time
import yaml
import os
import numpy as np

league_id = yaml.safe_load(open('config.yaml'))['league_id']

class Yahoo_Api():
    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token
                ):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._authorization = None
    def _login(self):
        global oauth
        oauth = OAuth2(None, None, from_file='oauth2yahoo.json')
        if not oauth.token_is_valid():
            oauth.refresh_access_token()

with open('oauth2yahoo.json') as json_yahoo_file:
    auths = json.load(json_yahoo_file)
yahoo_consumer_key = auths['consumer_key']
yahoo_consumer_secret = auths['consumer_secret']
yahoo_access_key = auths['access_token']
json_yahoo_file.close()

yahoo_api = Yahoo_Api(yahoo_consumer_key, yahoo_consumer_secret, yahoo_access_key)
yahoo_api._login()



url = 'https://fantasysports.yahooapis.com/fantasy/v2/game/nfl'.format(league_id)
response = oauth.session.get(url, params={'format': 'json'})
r = response.json()
print(r) #need the game id, add to config file
