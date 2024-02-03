import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text):
    # Tokenize the text
    words = word_tokenize(text)
    
    # Get the list of English stop words
    stop_words = set(stopwords.words('english'))
    
    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a sentence
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text
input_text = "This is an example sentence with some stop words."
output_text = remove_stop_words(input_text)
print("Original text:", input_text)
print("Text without stop words:", output_text)

