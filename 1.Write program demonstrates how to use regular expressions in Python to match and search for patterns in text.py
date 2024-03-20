import re


text = """
Alice: I wonder if I can match this pattern.
Bob: What pattern are you talking about?
Alice: It's something like 'pattern'.
"""


pattern = r"'(.*?)'"


matches = re.findall(pattern, text)


first_match = re.search(pattern, text)


print("All matches found:")
for match in matches:
    print(match)

if first_match:
    print("\nFirst match found:")
    print(first_match.group())
else:
    print("\nNo first match found.")
