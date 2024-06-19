import spacy

nlp = spacy.load("en_core_web_sm")

def named_entity_recognition(text):
    """
    Perform Named Entity Recognition (NER) on the input text.

    Args:
        text (str): The input text for NER.

    Returns:
        list: List of entities found in the text.
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
