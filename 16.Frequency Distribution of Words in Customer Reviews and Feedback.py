import pandas as pd
from collections import Counter
import string

df = pd.read_csv('reviews.csv')
text = df['review'].str.cat(sep=' ').lower()
text = text.translate(str.maketrans('', '', string.punctuation))
word_counts = Counter(text.split())
print(word_counts)
