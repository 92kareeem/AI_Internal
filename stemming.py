import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

text = "programming  programmed."

words = word_tokenize(text)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)