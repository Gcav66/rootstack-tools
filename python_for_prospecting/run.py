# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:57:51 2017

@author: Gus Cavanaugh
"""
import twitter
import pandas as pd

twitter_consumer_key = ''
twitter_consumer_secret = ''

twitter_access_token_key = ''
twitter_access_token_secret = ''

my_keywords = ["favorite", "love", "super"]

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

def find_good_tweets_mult(df, keywords):
    good_tweets_df = df[df['Tweets'].str.contains('|'.join(my_keywords))]
    return good_tweets_df

if __name__ == "__main__":
    uname = 'MCanalytics'
    foo = get_tweets(uname)
    tweets = format_tweets(foo)
    good_tweets = find_good_tweets_mult(tweets, my_keywords)
    print good_tweets
    
