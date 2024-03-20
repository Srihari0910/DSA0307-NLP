import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample text for Named Entity Recognition
text = "Apple Inc. is planning to open a new store in San Francisco next month."

# Process the text using SpaCy NLP pipeline
doc = nlp(text)

# Extract named entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the named entities
for entity in entities:
    print(f"Entity: {entity[0]}, Type: {entity[1]}")
