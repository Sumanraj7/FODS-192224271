import pandas as pd
from collections import Counter
import string
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return [word for word in text.split() if word not in stop_words]

df['processed_feedback'] = df['feedback'].apply(preprocess)
word_counts = Counter([word for words in df['processed_feedback'] for word in words])
N = int(input('Enter N: '))
top_words = word_counts.most_common(N)
words, counts = zip(*top_words)
plt.bar(words, counts)
plt.show()
