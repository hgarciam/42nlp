import matplotlib.pyplot as plt
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from random import randint

nltk.download('punkt')
nltk.download('stopwords')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.
    text_file = open('text.txt')
    text = text_file.read()
    print()
    #print(text[0:31])
    #print(type(text))
    print("Total number of characters:", len(text))

    sentences = sent_tokenize(text)
    print("Total number of sentences:", len(sentences))

    words = word_tokenize(text)
    print("Total number of words:", len(words))

    words_no_punct = []

    for w in words:
        if w.isalpha():
            words_no_punct.append(w.lower())

    print("Total number of words without punctuation:", len(words_no_punct))

    stop_words = stopwords.words("english")
    clean_words = []

    for w in words_no_punct:
        if w not in stop_words:
            clean_words.append(w)

    print("Total number of words without punctuation nor stopwords:", len(clean_words))

    #fdist = nltk.FreqDist(clean_words)
    #fdist.plot(40)
    #print(fdist.most_common(40))

    #plt.show()

    print(sentences[randint(0, len(sentences))])

if __name__ == '__main__':
    print_hi('NLP test')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
