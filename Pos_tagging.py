import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
text = "the cat sat on the mat."
words = word_tokenize(text)
tagged_words = pos_tag(words)
print("Part-of-Speech Tags:", tagged_words)
