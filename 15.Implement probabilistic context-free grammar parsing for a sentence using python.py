import nltk

# Define a simple probabilistic context-free grammar (PCFG)
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | N [0.3]
    VP -> V NP [0.9] | V [0.1]
    Det -> 'the' [1.0]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'chased' [0.7] | 'ate' [0.3]
""")

# Define a sentence to parse
sentence = "the dog chased the cat"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Create a probabilistic parser using Viterbi parsing algorithm
parser = nltk.ViterbiParser(pcfg_grammar)

# Parse the sentence using the parser
for tree in parser.parse(tokens):
    tree.pretty_print()
    print("Probability:", tree.prob())
