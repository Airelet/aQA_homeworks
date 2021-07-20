import re

sentences = []

with open('text.txt') as f:
    text_file = f.read()

print(text_file)

sentences = re.split(r'\.\s', text_file)
print(sentences)