# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = ['Hello, world!', 'I love this class!',
        'I am very hungry!']
for x in text:
    document = language_v1.Document(
        content=x, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={'document': document}).document_sentiment

    print("Text: {}".format(x))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
