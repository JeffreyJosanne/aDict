import os, codecs, re


def wordIn(word, phrase):
    return word in phrase.split()


def search(query):
    time = ''
    for file in os.listdir('subs/'):
        filePointer = codecs.open('subs/' + file, 'r', 'utf8')
        lines = filePointer.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            wordLists = line.split()
            for word in wordLists:
                re.sub('[^A-Za-z0-9]+', '', word)
                if query in word:
                    iterator = i
                    while True:
                        textFromLines = lines[iterator].split()
                        iterator = iterator - 1
                        if '-->' in textFromLines:
                            break
                        del textFromLines[:]
                    time = textFromLines[0]
                    break
    print(time)


search('me')
