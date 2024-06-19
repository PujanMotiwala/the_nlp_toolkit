from src.ner import named_entity_recognition

if __name__ == "__main__":
    sample_text = "Apple is looking at buying U.K. startup for $1 billion."
    entities = named_entity_recognition(sample_text)
    print("Named Entities:\n", entities)
