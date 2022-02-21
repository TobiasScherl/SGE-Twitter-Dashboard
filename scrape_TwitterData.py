import os
import pandas as pd
from tweepy import *
import tweepy
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_KEY_SECRET')
access_key= os.environ.get('TWITTER_ACCESS_TOKEN')
access_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

search_words = "SGE"      #enter your words
new_search = search_words + " -filter:retweets"

csvFile = open('SGE_2', 'a')
csvWriter = csv.writer(csvFile)

since_date = '2020-02-10'

for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=1000,
                           lang="de",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
    
df = pd.read_csv('SGE_2',names=["Date", "Tweet", "User", "Location"])

print(df.head())
