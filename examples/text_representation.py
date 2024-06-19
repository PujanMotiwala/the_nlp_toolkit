from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

documents = [
    "Natural Language Processing is fun.",
    "Machine Learning is fascinating.",
    "Deep Learning is a subset of Machine Learning."
]

# Bag of Words
count_vectorizer = CountVectorizer()
bow = count_vectorizer.fit_transform(documents)
print("Bag of Words:\n", bow.toarray())

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(documents)
print("TF-IDF:\n", tfidf.toarray())
