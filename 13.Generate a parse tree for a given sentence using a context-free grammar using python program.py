import nltk

# Define the context-free grammar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

# Define the sentence
sentence = "the cat chased the dog"

# Create a parser
parser = nltk.ChartParser(grammar)

# Parse the sentence and generate the parse tree
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
