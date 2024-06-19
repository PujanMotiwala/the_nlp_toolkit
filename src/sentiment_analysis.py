from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text.

    Args:
        text (str): Input text to analyze.

    Returns:
        Sentiment: Polarity and subjectivity of the text.
    """
    blob = TextBlob(text)
    return blob.sentiment
