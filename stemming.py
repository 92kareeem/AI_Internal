import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

# Example text
text = "programming  programmed."

# Tokenize the text into words
words = word_tokenize(text)

# Create a Porter stemmer
stemmer = PorterStemmer()

# Apply stemming to each word
stemmed_words = [stemmer.stem(word) for word in words]

# Print the results
print("Original Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)