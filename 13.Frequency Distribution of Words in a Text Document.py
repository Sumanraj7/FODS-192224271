from collections import Counter
import string

with open('sample_text.txt', 'r') as file:
    text = file.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

words = text.split()

word_counts = Counter(words)

for word, count in word_counts.items():
    print(f'{word}: {count}')
