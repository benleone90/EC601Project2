import tweepy

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


# TWITTER CLIENT #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().auth_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets


# TWITTER AUTHENTICATOR #
class TwitterAuthenticator():
    def auth_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# TWITTER STREAMER #
class TwitterStream():
    # Class for streaming and processing live tweets.

    def __init__(self):
        self.twitter_auth = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets, hashtag_list):
        # This handles Twitter authentication and connection to the Twitter Streaming API.
        listener = TwitterListener(fetched_tweets)
        auth = self.twitter_auth.auth_twitter_app()
        stream = Stream(auth, listener)

        # This line filters Twitter streams to capture data by the keywords
        stream.filter(track=hashtag_list)


# TWITTER STREAMER LISTENER #
class TwitterListener(StreamListener):
    # Basic listener class that prints received tweets to stdout.
    def __init__(self, fetched_tweets):
        self.fetched_tweets = fetched_tweets

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method (increase your calm)
            return False
        print(status)


if __name__ == "__main__":
    hashtag_list = ["Ruth Bader Ginsburg"]
    fetched_tweets = "tweets.json"

    twitter_client = TwitterClient('benshapiro')
    print(twitter_client.get_user_tweets(1))
    # twitter_streamer = TwitterStream()
    # twitter_streamer.stream_tweets(fetched_tweets, hashtag_list)
