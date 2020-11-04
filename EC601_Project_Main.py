# Imports from the Tweepy Library
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor


# Imports the Google Cloud client library
from google.cloud import language_v1

# Imports Twitter API credentials and creates Google NPL client
import twitter_credentials
client = language_v1.LanguageServiceClient()

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
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user, tweet_mode='extended').items(num_tweets):
            tweets.append(tweet.full_text)
        return tweets

# MAIN FUNCTION #
# if __name__ == "__main__":
    # print("##########################\n\nWelcome to Tweet Analyzer!\n\n##########################")
    # prog_input = 0
    # prog_input = input(
    #     "Which program would you like to run?\n 1. User tweet sentiment analyzer (@username, # tweets)\n 2. Compare two users most recent tweet sentiment (@username, @username)\nProgram: ")
    # if int(prog_input) == 1:
    #     t_handle = input("Enter user's Twitter handle (after the @): ")
    #     tweet_nums = int(input("Enter # of tweets to analyze: "))
    #     twitter_client = TwitterClient(t_handle)
    #     twitter_client.get_user_tweets(tweet_nums)
    #     for x in tweets:
    #         document = types.Document(
    #             content=x, type=enums.Document.Type.PLAIN_TEXT)
    #         # Detects the sentiment of the text
    #         sentiment = client.analyze_sentiment(
    #             document=document).document_sentiment
    #         print("Tweet text: {}".format(x))
    #         print("Sentiment score(-1.0 to 1.0): {}".format(sentiment.score))
    #         print("Sentiment magnitue(0 to inf): {}".format(sentiment.magnitude))
    # elif int(prog_input) == 2:
    #     person1 = input("Enter first user's twitter handle (after the @): ")
    #     twitter_client1 = TwitterClient(person1)
    #     twitter_client1.get_user_tweets(1)
    #     for x in tweets:
    #         document1 = types.Document(
    #             content=x, type=enums.Document.Type.PLAIN_TEXT)
    #         # Detects the sentiment of the text
    #         sentiment1 = client.analyze_sentiment(
    #             document=document1).document_sentiment
    #     tweet1 = tweets[0]
    #     score1 = sentiment1.score
    #     magnitude1 = sentiment1.magnitude
    #     ####################################
    #     tweets.clear()
    #     person2 = input("Enter second user's twitter handle (after the @): ")
    #     twitter_client2 = TwitterClient(person2)
    #     twitter_client2.get_user_tweets(1)
    #     for x in tweets:
    #         document2 = types.Document(
    #             content=x, type=enums.Document.Type.PLAIN_TEXT)
    #         sentiment2 = client.analyze_sentiment(
    #             document=document2).document_sentiment
    #     tweet2 = tweets[0]
    #     score2 = sentiment2.score
    #     magnitude2 = sentiment2.magnitude
    #     print(person1 + "'s tweet: " + tweet1)
    #     print("Sentiment score: " + score1)
    #     print(person2 + "'s tweet: " + tweet2)
    #     print("Sentiemet score: " + score2)
    #     print("##########################")
    #     if score1 > score2:
    #         print(person1 + " has a higher sentiment score")
    #     else:
    #         print(person2 + " has a higher sentiment score")
    # else:
    #     print("Invalid program")
    #     exit()
