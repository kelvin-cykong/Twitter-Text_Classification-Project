#### Twitter API for Extracting Twitter Text Data ####
### Created by Kelvin Kong ###
### Last Modified on June 6 2022 ###

### We Use Twitter API v2 ###
import tweepy
import time
from datetime import datetime

# Personal Twitter Dev Credentials
# developer.twitter.com
api_key = "api_key"
api_key_secret = "api_key_secret" 

access_token = "access-token" 
access_token_secret = "access-token-secret" 

bearerToken = "bearer-token"
# Obtain Details from Twitter Dev Website

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Program Time: ", current_time)

#### Use this Code if you plan to use api_keys and access_token
# client = tweepy.Client(
#    consumer_key = api_key, 
#    consumer_secret = api_key_secret, 
#    access_token = accessToken, 
#    access_token_secret = accessTokenSecret
#)
### End of Section

#### Use this code if you plan to use bearer token only
client = tweepy.Client(bearer_token = bearerToken)
### End of Section

#Specify Query
Query = 'iPhone -is:retweet'

results = client.search_recent_tweets(query = Query, tweet_fields = ['context_annotations', 'created_at'], max_result=100) 

# Print Result

for result in results.data:
    print(result.text)
    if len(result.context_annotations) > 0:
        print(result.context_annotations)


# Let Tweepy sleep 15mins
print("Wait the API to response in 15 mins after each run")

for i in range(901):
    print("Time Elipsed " + str(i+1) + " seconds", end="\r")
    time.sleep(1) 