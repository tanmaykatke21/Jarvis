import numpy as np
import nltk 
from nltk.stem.porter import PorterStemmer

#creating an object where all our data will come and we will store it and work on it
Stemmer=PorterStemmer()

def tokenize(sentence): #to tokenize
    return nltk.word_tokenize(sentence)

def stem(word): #to convert into words
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word=[stem(word) for word in tokenized_sentence]
    bag=np.zeros(len(words),dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx]=1
    return bag