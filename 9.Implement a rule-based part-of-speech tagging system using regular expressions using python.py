import re

# Sample text for tagging
text = "The quick brown fox jumps over the lazy dog."

# Define regular expression patterns and corresponding POS tags
patterns = [
    (r'\bThe\b', 'DT'),      # Determiner
    (r'\bquick\b', 'JJ'),    # Adjective
    (r'\bbrown\b', 'JJ'),    # Adjective
    (r'\bfox\b', 'NN'),      # Noun
    (r'\bjumps\b', 'VBZ'),   # Verb
    (r'\bover\b', 'IN'),     # Preposition
    (r'\bthe\b', 'DT'),      # Determiner
    (r'\blazy\b', 'JJ'),     # Adjective
    (r'\bdog\b', 'NN'),      # Noun
]

# Perform rule-based POS tagging
pos_tags = []
for word in text.split():
    tagged = False
    for pattern, pos_tag in patterns:
        if re.match(pattern, word, re.I):  # Case-insensitive match
            pos_tags.append((word, pos_tag))
            tagged = True
            break
    if not tagged:
        pos_tags.append((word, 'Unknown'))

# Print the tagged words
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
