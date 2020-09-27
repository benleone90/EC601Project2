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

# Imports Twitter API credentials and creates Google NPL client
import twitter_credentials
client = language.LanguageServiceClient()

# Empty array for tweets to be filled
# by Twitter client and analyzed by Goole NLP
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
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user, tweet_mode="extended").items(num_tweets):
            tweets.append(tweet.full_text)

    def twitter_client_api(self):
        return self.twitter_client


# Main function
if __name__ == "__main__":
    print("##########################\n\nWelcome to Tweet Analyzer!\n\n##########################")
    prog_input = 0
    prog_input = input(
        "Which program would you like to run?\n 1. User tweet sentiment analyzer (@username, # tweets)\n 2. Compare two users most recent tweet sentiment (@username, @username)\nProgram: ")
    if int(prog_input) == 1:
        t_handle = input("Enter user's Twitter handle (after the @): ")
        tweet_nums = int(input("Enter # of tweets to analyze: "))
        twitter_client = TwitterClient(t_handle)
        twitter_client.get_user_tweets(tweet_nums)
        for x in tweets:
            document = types.Document(
                content=x, type=enums.Document.Type.PLAIN_TEXT)
            # Detects the sentiment of the text
            sentiment = client.analyze_sentiment(
                document=document).document_sentiment
            print("Tweet text: {}".format(x))
            print("Sentiment score(-1.0 to 1.0): {}".format(sentiment.score))
            print("Sentiment magnitue(0 to inf): {}".format(sentiment.magnitude))
    elif prog_input == 2:
        print("Program 2")
    else:
        print("Invalid program")
        exit()
