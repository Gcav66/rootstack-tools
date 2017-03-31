# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:37:50 2017

@author: Gus Cavanaugh
"""

import twitter
import pandas as pd

twitter_consumer_key = 'XXXXXXXXXXX'
twitter_consumer_secret = 'XXXXXXXXXX'

twitter_access_token_key = 'XXXXXXXXXXXXXXXXXX'
twitter_access_token_secret = 'XXXXXXXXXXXXXXXX'

def get_tweets(username):
    api = twitter.Api(consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=twitter_access_token_key,
                      access_token_secret=twitter_access_token_secret)
    
    statuses = api.GetUserTimeline(screen_name=username, count=200)
    return statuses

def format_tweets(statuses):       
    mytweets = {'Tweets': [x.text for x in statuses]}
    df = pd.DataFrame(mytweets)
    return df

def find_good_tweets(df):
    keyword = 'favorite'
    good_tweets_df = df[df['Tweets'].str.contains(keyword)]
    return good_tweets_df


if __name__ == "__main__":
    print "Hello World"
    uname = 'MCanalytics'
    foo = get_tweets(uname)
    tweets = format_tweets(foo)
    good_tweets = find_good_tweets(tweets)
    print good_tweets
    