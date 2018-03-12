import tweepy
import random
import time

consumer_key = <consumer_secret>
consumer_secret = <consumer_secret>
access_token = <access_token>
access_token_secret = <access_token_secret>

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)

def split_tweet(tweet,max_tweet_length):
    splitted_tweet = tweet.split(' ')
    idx = 0
    new_tweet=[]

    while len(' '.join(new_tweet)) < len(tweet):
        temp_tweet = []
        while len(' '.join(temp_tweet)) < max_tweet_length:
            temp_tweet.append(splitted_tweet[idx])
            idx += 1
            if idx == len(splitted_tweet):
                break
        new_tweet.append(' '.join(temp_tweet))

    return new_tweet


if __name__ == "__main__":
    fname = <path/to/thesis/txtfile>
    # fname = "./tese_long_utf8.txt"
    with open(fname) as f:
        content = f.read().splitlines()

    max_tweet_length = 118
    tweet_interval = 3

    tweet = random.choice(content)


    if len(tweet) > max_tweet_length:
        new_tweet = split_tweet(tweet,max_tweet_length)
        for i in range(len(new_tweet)):
            tweet="{} ({}/{})".format(new_tweet[i],(i+1),len(new_tweet))
            if i == 0:
                API.update_status(status=tweet)
            else:
                API.update_status(status=tweet, in_reply_to_status_id=API.user_timeline()[0].id)
            time.sleep(tweet_interval)
    else:
        API.update_status(status=tweet)
