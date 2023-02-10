# Import necessary libraries
import os
import pandas as pd
from tweepy import *
import tweepy
import pandas as pd
import csv
import re 
import string
import preprocessor as p

# Get Twitter API keys from environment variables
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_KEY_SECRET')
access_key= os.environ.get('TWITTER_ACCESS_TOKEN')
access_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Create OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

#Initialize API
api = tweepy.API(auth,wait_on_rate_limit=True)

#Specify search word and create a new search (retweets filtered out)
search_words = "SGE"
new_search = search_words + " -filter:retweets"

#Open csv file to which results will be written
csvFile = open('SGE_6', 'a')
csvWriter = csv.writer(csvFile)

# Call the tweepy Cursor with specified arguments like language "de" and write results to csv file
for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=1000,
                           lang="de",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])