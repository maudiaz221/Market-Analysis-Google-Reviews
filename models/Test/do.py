import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



stop_words = set(stopwords.words('english'))





def resumeReview(text):
    stop_words = set(stopwords.words('english'))
    split = text.split(' ')

    filter = []
    for word in split:
        if word not in stop_words:
            filter.append(word)

    return filter



text = 'oh my god this sandwhich is so good the lettuce has so much quality'

fin = resumeReview(text)
print(fin)

