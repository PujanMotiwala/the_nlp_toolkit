from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

if __name__ == "__main__":
    sample_text = "Natural Language Processing with Python is fun and exciting!"
    sentiment = analyze_sentiment(sample_text)
    print("Sentiment Analysis:\n", sentiment)
