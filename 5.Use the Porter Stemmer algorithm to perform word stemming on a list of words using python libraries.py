import nltk
from nltk.stem import PorterStemmer

def perform_stemming(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def main():
    nltk.download('punkt')  # Download required data for tokenization
    words = ["running", "easily", "quickly", "beautifully", "friendships", "friendship", "friends"]
    stemmed_words = perform_stemming(words)
    for original, stemmed in zip(words, stemmed_words):
        print(f"{original} -> {stemmed}")

if __name__ == "__main__":
    main()
