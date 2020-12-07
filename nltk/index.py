# ntlk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
import nltk

text = """A Topic in Kafka is something where a message is sent. The consumer applications which are 
interested in that topic pulls the message inside that topic and can do anything with that data. Up 
to a specific time, any number of consumer applications can pull this message any number of times."""

sentences = sent_tokenize(text)
print(sentences)

words = word_tokenize(text)
print(words)

distribution = FreqDist(words)
print(distribution.most_common(2))

language = "english"
stop_words = set(stopwords.words(language))
print(stop_words)

filtered_words = []

for word in words:
    if word not in stop_words:
        filtered_words.append(word)
        
print(filtered_words)


ps = PorterStemmer()
stemmed_words = []
for word in filtered_words:
    stemmed_words.append(ps.stem(word))

print("Stemmed Sentence:", stemmed_words)

tokens = word_tokenize(sentences[0])
print(tokens)