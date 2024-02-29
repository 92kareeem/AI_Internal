import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

str1 = "Remove stop words from this sentence using NLTK."
str2 = "NLTK is powerful tool for natural language processing."
str3 = "Stop words are common words that are often excluded in text analysis."

def stop_words_removal(text):
  words = word_tokenize(text)
  stop_words = set(stopwords.words('english'))
  print("Original text: ", text)
  filtered_words = [word for word in words if word.lower() not in stop_words]
  filtered_text = ' '.join(filtered_words)
  print("Filtered Text: ", filtered_text)

stop_words_removal(str1)
stop_words_removal(str2)
stop_words_removal(str3)
