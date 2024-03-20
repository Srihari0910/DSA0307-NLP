import random

# Sample text for training the bigram model
corpus = "The quick brown fox jumps over the lazy dog. The quick brown fox is fast. The lazy dog is sleeping."

# Tokenize the text into words
words = corpus.split()

# Create a dictionary to store bigram frequencies
bigrams = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in bigrams:
        bigrams[current_word] = []
    bigrams[current_word].append(next_word)

# Generate text using the bigram model
starting_word = random.choice(words)
generated_text = [starting_word]
for _ in range(20):  # Generate 20 words
    if starting_word in bigrams:
        next_word = random.choice(bigrams[starting_word])
        generated_text.append(next_word)
        starting_word = next_word
    else:
        break

generated_text = " ".join(generated_text)
print(generated_text)

