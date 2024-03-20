import random

# Sample training data with (word, POS tag) pairs
training_data = [
    ("The", "DT"),
    ("quick", "JJ"),
    ("brown", "JJ"),
    ("fox", "NN"),
    ("jumps", "VBZ"),
    ("over", "IN"),
    ("the", "DT"),
    ("lazy", "JJ"),
    ("dog", "NN"),
    (".", "."),
]

# Define a function to train the probabilistic model
def train_pos_tagger(training_data):
    pos_model = {}
    for word, pos_tag in training_data:
        if pos_tag not in pos_model:
            pos_model[pos_tag] = []
        pos_model[pos_tag].append(word)
    return pos_model

# Train the POS tagger
pos_model = train_pos_tagger(training_data)

# Sample text for tagging
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = text.split()

# Perform stochastic POS tagging
pos_tags = []
for word in words:
    if word in pos_model:
        possible_tags = pos_model[word]
        selected_tag = random.choice(possible_tags)
        pos_tags.append((word, selected_tag))
    else:
        pos_tags.append((word, "Unknown"))

# Print the tagged words
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
