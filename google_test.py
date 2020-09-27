# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = ['Hello, world!', 'this class sucks!', 'where is the bathroom?']
for x in text:
    document = types.Document(
        content=x,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(x))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
