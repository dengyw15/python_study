from nltk.corpus import movie_reviews
from nltk import FreqDist
import random
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
# print(movie_reviews.categories())
random.shuffle(documents)
print(movie_reviews.words())
all_words = FreqDist(w.lower() for w in movie_reviews.words())
print(all_words)
word_features = all_words.keys()[:2000]


def document_features(document):
    documents_word = set(documents)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in documents_word)
    return features

print(document_features(movie_reviews.words('pos/cv957_8737.txt')))