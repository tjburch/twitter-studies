#Import the necessary methods from tweepy library
import tweepy
from access import access_token, access_token_secret, consumer_key, consumer_secret # This is everything contained in that file
import datetime
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Method for someone else
# user = api.get_user()

# Method for me
user = api.me()

quantities_of_interest = ['created_at','favorite_count','retweet_count']

with open('data/mytweets.csv','w+') as csv_file:
    csv_file.write( (','.join(quantities_of_interest))+'\n' )

    for tweet in tweepy.Cursor(api.user_timeline, user).items():
        if tweet.created_at < datetime.datetime(2015,1,1): continue
        # Prune data for original tweets
        if tweet.in_reply_to_status_id is not None: continue
        if tweet.retweeted: continue
        
        write_list =[]
        for q in quantities_of_interest:
            write_list.append(str(tweet._json[q]))
        csv_file.write(','.join(write_list))
        csv_file.write('\n')