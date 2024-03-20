# Sample text for tagging
text = "The quick brown fox jumps over the lazy dog."

# Define initial POS tags for each word
initial_tags = {
    "The": "DT",
    "quick": "JJ",
    "brown": "JJ",
    "fox": "NN",
    "jumps": "VB",
    "over": "IN",
    "the": "DT",
    "lazy": "JJ",
    "dog": "NN",
}

# Define a transformation rule
transformation_rule = {
    "quick": "RB",  # Change "quick" from adjective to adverb
    "jumps": "VBZ",  # Change "jumps" from verb to verb with 3rd person singular
    "dog": "NNS",  # Change "dog" from singular noun to plural noun
}

# Apply the transformation rule to update POS tags
for word, initial_tag in initial_tags.items():
    if word in transformation_rule:
        initial_tags[word] = transformation_rule[word]

# Print the tagged words after applying the transformation rule
for word, pos_tag in initial_tags.items():
    print(f"{word}: {pos_tag}")
