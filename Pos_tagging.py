import nltk

# Download the missing resource
nltk.download('averaged_perceptron_tagger')

# Now, you should be able to use the pos_tag function without errors
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Example text
text = "the cat sat on the mat."

# Tokenize the text into words
words = word_tokenize(text)

# Part-of-speech tagging
tagged_words = pos_tag(words)
print("Part-of-Speech Tags:", tagged_words)