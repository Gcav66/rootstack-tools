# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:50:06 2017

@author: Gus Cavanaugh
"""

import twitter
import pandas as pd

twitter_consumer_key = 'NRC0vAPxEOq1tOpY9qeFng'
twitter_consumer_secret = 'ivIQOgPyuhoNjlPpVslM4837VGaq9r76vKQ5YUuh020'

twitter_access_token_key = '325235411-gdyxbcvrjoSANEsHHfcytaJFeRYFIlZn3XsPgstl'
twitter_access_token_secret = '6RL5KhNOz655K5ZQ3kF2dBtAosDZwISy8rSzgVHfr1s'

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
    #flat = df.set_index('Tweets')
    #return flat
    return df


if __name__ == "__main__":
    print "Hello World"
    uname = 'MCanalytics'
    raw_tweets = get_tweets(uname)
    print raw_tweets
    #tweets = format_tweets(foo)
    #print tweets.head()
    