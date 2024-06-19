from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def get_bag_of_words(documents):
    """
    Convert a collection of text documents to a matrix of token counts (Bag of Words).

    Args:
        documents (list of str): List of text documents.

    Returns:
        array: Bag of Words representation of the documents.
    """
    vectorizer = CountVectorizer()
    bow = vectorizer.fit_transform(documents)
    return bow.toarray()

def get_tfidf(documents):
    """
    Convert a collection of raw documents to a matrix of TF-IDF features.

    Args:
        documents (list of str): List of text documents.

    Returns:
        array: TF-IDF representation of the documents.
    """
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)
    return tfidf.toarray()
