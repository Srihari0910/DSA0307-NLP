import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def resolve_references(text):
    # Process the text using spaCy
    doc = nlp(text)

    # Create a dictionary to store resolved references
    references = {}

    # Iterate through tokens in the document
    for token in doc:
        if token.dep_ in ["pronoun"]:
            # Check if the token is a pronoun and resolve its reference
            resolved_reference = find_antecedent(token)

            # Store the resolved reference in the dictionary
            references[token.text] = resolved_reference

    # Replace pronouns with resolved references in the text
    resolved_text = " ".join(references.get(token.text, token.text) for token in doc)

    return resolved_text

def find_antecedent(pronoun_token):
    # Find the antecedent of the pronoun by traversing the dependency tree
    for ancestor in pronoun_token.ancestors:
        if ancestor.dep_ in ["nsubj", "attr"]:
            return ancestor.text

    # If no antecedent is found, check for previous sentences
    for sentence in pronoun_token.doc.sents:
        for token in sentence:
            if token.dep_ in ["nsubj", "attr"]:
                return token.text

    # Return an empty string if no antecedent is found
    return ""

if __name__ == "__main__":
    # Example text with references
    example_text = "John has a cat. He loves it. The cat is very playful."

    # Perform reference resolution
    resolved_text = resolve_references(example_text)

    # Print the original and resolved texts
    print("Original Text:")
    print(example_text)
    print("\nResolved Text:")
    print(resolved_text)
