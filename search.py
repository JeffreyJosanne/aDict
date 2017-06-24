import os, codecs, re


def wordIn(word, phrase):
    return word in phrase.split()


def search(query):
    for file in os.listdir('subs/'):
        with codecs.open('subs/' + file, 'r', 'utf8') as lines:
            for line in lines:
                wordLists = line.split()
                for word in wordLists:
                    re.sub('[^A-Za-z0-9]+', '', word)
                    if query is word:
                        print(line)


search('Hey')
