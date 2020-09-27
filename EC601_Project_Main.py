# Imports from the Tweepy Library
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
# from tweepy import Stream
# from tweepy.streaming import StreamListener

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Imports Twitter API credentials
import twitter_credentials

# Empty array for tweets to be filled by Twitter client
# and analyzed by Goole NLP
tweets = []

# Twitter Authenticator


class TwitterAuthenticator():
    def auth_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# Twitter Client
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().auth_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_tweets(self, num_tweets):
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)

    def twitter_client_api(self):
        return self.twitter_client


# Main function
if __name__ == "__main__":
    twitter_client = TwitterClient()
    api = twitter_client.twitter_client_api()

    status = api.user_timeline("ben_leone", tweet_mode="extended")
    print(status.full_text)
    ######################
    # person1 = input("Enter first person: ")
    # num = int(input("How many tweets would you like to see: "))
    # twitter_client = TwitterClient(person1)
    # twitter_client.get_user_tweets(num)
    # for x in tweets:
    # print(x)
