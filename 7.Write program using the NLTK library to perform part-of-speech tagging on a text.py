import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text for POS tagging
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the POS-tagged words
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")

