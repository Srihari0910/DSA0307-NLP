import random

class SimplePOSTagger:
    def __init__(self, transition_probs, emission_probs):
        """
        Initialize the POS tagger with transition and emission probabilities.
        
        transition_probs: dict of transition probabilities from one POS tag to another
        emission_probs: dict of emission probabilities of words given their POS tags
        """
        self.transition_probs = transition_probs
        self.emission_probs = emission_probs
    
    def tag(self, sentence):
        """
        Tag a sentence with POS tags.
        
        sentence: list of words in the sentence
        """
        tagged_sentence = []
        prev_tag = None
        
        for word in sentence:
            if word in self.emission_probs:
                pos_tags = list(self.emission_probs[word].keys())
                # Choose a POS tag for the word based on emission probabilities
                tag = random.choices(pos_tags, weights=self.emission_probs[word].values())[0]
            else:
                # If word not found in emission probabilities, assign a random tag
                tag = random.choice(list(self.transition_probs.keys()))
            
            # Use transition probabilities if there's a previous tag
            if prev_tag:
                if prev_tag in self.transition_probs and tag in self.transition_probs[prev_tag]:
                    tag = random.choices([tag, prev_tag], 
                                         weights=[self.transition_probs[prev_tag][tag], 
                                                  1 - self.transition_probs[prev_tag][tag]])[0]
            tagged_sentence.append((word, tag))
            prev_tag = tag
        
        return tagged_sentence

# Example usage
transition_probs = {
    'NOUN': {'NOUN': 0.7, 'VERB': 0.2, 'ADJ': 0.1},
    'VERB': {'NOUN': 0.3, 'VERB': 0.4, 'ADJ': 0.3},
    'ADJ': {'NOUN': 0.4, 'VERB': 0.3, 'ADJ': 0.3}
}

emission_probs = {
    'apple': {'NOUN': 0.9, 'VERB': 0.1},
    'eat': {'VERB': 0.9, 'NOUN': 0.1},
    'red': {'ADJ': 0.8, 'NOUN': 0.1, 'VERB': 0.1}
}

tagger = SimplePOSTagger(transition_probs, emission_probs)
sentence = ['I', 'eat', 'a', 'red', 'apple']
tagged_sentence = tagger.tag(sentence)
print(tagged_sentence)
