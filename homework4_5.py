import re

sentences = []

with open('text.txt') as f:
    text_file = f.read()

# print(text_file)
# text_file variable it is just text not a file or I/O wrapper

sentences = re.split(r'\.\s', text_file)
# print(sentences)
for sentence in sentences:
    print()
    print(sentence)
# Well it is works but '.' symbol is not in result
# Take a look how it could be done with another regular expression.
for sentence in re.findall(r"[А-Я].*?[.!?](?=\s|$)", text_file):
    print()
    print(sentence)