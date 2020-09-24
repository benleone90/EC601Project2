import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStream():
    # Class for streaming and processing live tweets.
    def stream_tweets(self, fetched_tweets, hashtag_list):
        # This handles Twitter authentication and connection to the Twitter Streaming API.
        listener = StdOutListener(fetched_tweets)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track=hashtag_list)


class StdOutListener(StreamListener):
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
        print(status)


if __name__ == "__main__":
    hashtag_list = ["donald trump", "hillary clinton",
                    "barack obama", "bernie sanders"]
    fetched_tweets = "tweets.json"

    twitter_streamer = twitter_streamer()
    twitter_streamer.stream_tweets(fetched_tweets, hashtag_list)
