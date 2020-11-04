from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

import twitter_credentials


# TWITTER AUTHENTICATOR #
class TwitterAuthenticator():
    def auth_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_SECRET)
        return auth


# TWITTER CLIENT #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().auth_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user, tweet_mode='extended').items(num_tweets):
            tweets.append(tweet.full_text)
        return tweets


if __name__ == "__main__":
    client = TwitterClient('ben_leone')
    print(client.get_user_timeline_tweets(5))
