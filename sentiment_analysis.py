import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob
import time
from spacy.language import Language

class Sentiment:
    """
    Class to determine and represent the sentiment of a set of text
    """
    
    POSITIVE = 1
    NEUTRAL  = 0
    NEGATIVE = -1

    category = None
    polarity = None

    def __init__(self, polarity):
        """
        Sentiment constructor that takes the polarity value from a sentiment analysis
        and assigns a category of sentiment

        Parameters:
        - polarity: the polarity value from a sentiment analysis
        """

        self.polarity = polarity
        match polarity:
            case POSITIVE if polarity > 0.333:
                self.category = Sentiment.POSITIVE
            case NEGATIVE if polarity < -0.333:
                self.category = Sentiment.NEGATIVE
            case _:
                self.category = Sentiment.NEUTRAL

    def toString(category):
        """
        Converts the sentiment to a string value

        Parameters:
        - category: the category of sentiment

        Returns:
        The sentiment as a string
        """
        match category:
            case POSITIVE if category == Sentiment.POSITIVE:
                return "Positive"
            case NEGATIVE if category == Sentiment.NEGATIVE:
                return "Negative"
            case NEUTRAL if category == Sentiment.NEUTRAL:
                return "Neutral"
            case _:
                return "Invalid"


def getSentiment(text):
    """
    Determines the sentiment of a given set of text

    Parameters:
    - text: a set of text

    Returns:
    A Sentiment object for the text
    """
    
    # Get a cleaned NLP document for the review
    doc = nlp(str([token.text.lower().strip() for token in nlp(text) if not token.is_stop]))

    # return sentiment
    return Sentiment(doc._.blob.polarity)

def generateSentiments(category, count, data):
    """
    Generate sentiments for a particular category, from a limited set of text from a dataset

    Parameters:
    - category: the category of sentiment to search for
    - count:    the maximum number of results
    - data:     the dataset containing the text to analyse
    """
    
    # Print the category as a header
    print("".ljust(80, '#'))
    print('### ', Sentiment.toString(category), 'Reviews')
    print("".ljust(80, '#'))

    total = 0

    # Process each text in the dataset until the maximum number of results in 
    #   the category has been printed
    for text in data:
        
        # Determine the sentiment of the text
        sentiment = getSentiment(text)

        # Print the review text if the sentiment matches the required category
        if sentiment.category == category:
            print(' >', text)
            total += 1

        # Break if we have reached the maximum number
        if total >= count:
            break

# Load the Load the 'en_core_web_sm' spaCy model 
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Read in the sample dataset of Amazon product consumer reviews
dataframe = pd.read_csv('amazon_product_reviews.csv')

# Get the review text data, excluding blank entries
clean_data = dataframe.dropna(subset=['reviews.text'])['reviews.text']

# Generate sentiments for each category
count = 10
generateSentiments(Sentiment.POSITIVE, count, clean_data)
generateSentiments(Sentiment.NEUTRAL,  count, clean_data)
generateSentiments(Sentiment.NEGATIVE, count, clean_data)

print()
