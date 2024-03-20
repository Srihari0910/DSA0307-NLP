from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Function to implement Lesk algorithm for word sense disambiguation
def lesk(word, sentence):
    best_sense = None
    max_overlap = 0

    word = word.lower()
    sentence = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stopwords.words('english')]

    synsets = wordnet.synsets(word)

    for sense in synsets:
        definition = sense.definition()
        examples = sense.examples()
        gloss = set(word_tokenize(definition))
        for example in examples:
            gloss.update(set(word_tokenize(example)))
        overlap = len(gloss.intersection(set(sentence)))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage:
if __name__ == "__main__":
    word = "bank"
    sentence = "He sat on the bank of the river and watched the boats."

    sense = lesk(word, sentence)
    if sense:
        print("Word:", word)
        print("Sentence:", sentence)
        print("Best Sense:", sense.name())
        print("Definition:", sense.definition())
    else:
        print("No sense found for the word.")
