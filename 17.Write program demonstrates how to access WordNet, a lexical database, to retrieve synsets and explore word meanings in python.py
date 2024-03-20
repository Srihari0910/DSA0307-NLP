from nltk.corpus import wordnet

# Function to explore word meanings
def explore_word(word):
    synsets = wordnet.synsets(word)
    if synsets:
        print(f"Word: {word}")
        for synset in synsets:
            print(f"Synset: {synset.name()}")
            print(f"Definition: {synset.definition()}")
            print(f"Examples: {synset.examples()}")
            print()
    else:
        print(f"No synsets found for the word '{word}'.")

# Example word
word = "play"

# Explore word meanings
explore_word(word)
