# Introduction to The_NLP_Toolkit

Welcome to **The_NLP_Toolkit**. This document provides an overview of the various NLP techniques covered in this repository. Each technique is accompanied by practical examples and detailed explanations to help you understand and implement them in your projects.

# NLP Techniques

## Named Entity Recognition (NER)

Named Entity Recognition (NER) is the process of locating and classifying named entities in text into predefined categories such as person names, organizations, locations, etc.

### Usage

The `named_entity_recognition` function in the `ner` module performs NER using spaCy.

#### Example

```python
from src.ner import named_entity_recognition

text = "Apple is looking at buying U.K. startup for $1 billion."
entities = named_entity_recognition(text)
print(entities)
