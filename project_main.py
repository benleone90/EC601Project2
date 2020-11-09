from os import system
# Imports from the Tweepy Library
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

# Imports the Google Cloud client library
from google.cloud import language_v1

# Imports Twitter API credentials and creates Google NPL client
import twitter_credentials

# Empty array for tweets to be filled
# by Twitter client and analyzed by Goole NLP
tweets = []


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
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user, tweet_mode='extended').items(num_tweets):
            tweets.append(tweet.full_text)
        return tweets


# ANALYZE TWEET #
class TwitterAnalysis():
    def analyze_tweet(self, text):
        self.client = language_v1.LanguageServiceClient()
        self.document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        self.sentiment = self.client.analyze_sentiment(
            request={'document': self.document}).document_sentiment
        print(u"Tweet Text: {}".format(text))
        print(u"Sentiment score(-1.0 to 1.0): {}".format(self.sentiment.score))
        print(u"Sentiment magnitue(0 to \u221e): {}".format(
            self.sentiment.magnitude))

    def compare_tweets(self, text):
        self.client = language_v1.LanguageServiceClient()
        self.document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        self.sentiment = self.client.analyze_sentiment(
            request={'document': self.document}).document_sentiment
        return self.sentiment


# MAIN FUNCTION #
if __name__ == "__main__":
    system('clear')
    print("##########################\n\nWelcome to Tweet Analyzer!\n\n##########################")
    program = 0
    program = input(
        "Which program would you like to run?\n 1. User tweet sentiment analyzer (@username, # tweets)\n 2. Compare the sentiment of two user's most recent tweet (@username, @username)\nProgram: ")
    system('clear')
    if int(program) == 1:
        username = input("Enter user's Twitter handle (after the @): ")
        amount = int(input("Enter # of tweets to analyze: "))
        client = TwitterClient(username)
        client.get_user_timeline_tweets(amount)
        for x in tweets:
            print("\n")
            TwitterAnalysis().analyze_tweet(x)
    elif int(program) == 2:
        username1 = input("Enter first user's twitter handle (after the @): ")
        client1 = TwitterClient(username1)
        client1.get_user_timeline_tweets(1)
        for x in tweets:
            sentiment_1 = TwitterAnalysis().compare_tweets(x)
        tweet1 = tweets[0]
        score1 = sentiment_1.score
        magnitude1 = sentiment_1.magnitude
        ####################################
        tweets.clear()
        username2 = input("Enter second user's twitter handle (after the @): ")
        client2 = TwitterClient(username2)
        client2.get_user_timeline_tweets(1)
        for x in tweets:
            sentiment_2 = TwitterAnalysis().compare_tweets(x)
        tweet2 = tweets[0]
        score2 = sentiment_2.score
        magnitude2 = sentiment_2.magnitude
        system('clear')
        print(username1 + "'s tweet: " + tweet1)
        print("Sentiment score: ", score1)
        print(username2 + "'s tweet: " + tweet2)
        print("Sentiemet score: ", score2)
        print("#############################################")
        if score1 > score2:
            print(username1 + " has a higher sentiment score")
        else:
            print(username2 + " has a higher sentiment score")
    else:
        print("Invalid program")
        exit()
