from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

sentence = "saya mahasiswa rajin dan tidak sombong"
words = word_tokenize(sentence)

for word in words:
    print(word + ":" + ps.stem(word))
