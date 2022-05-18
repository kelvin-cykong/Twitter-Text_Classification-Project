#### Twitter API for Extracting Twitter Text Data ####
### Created by Kelvin Kong ###
### Last Modified on May 16 2022 ###

### We Use Twitter API v2 ###
from tweepy import OAuthHandler
from tweepy.streaming import Stream #Tweepy Update to import Stream
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time

# Personal Twitter Dev Credentials
# developer.twitter.com
api_key = "api_key"
api_key_secret = "api_key_secret" 

access_token = "access-token" 
access_token_secret = "access-token-secret" 
# Obtain Details from Twitter Dev Website

auth = OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

