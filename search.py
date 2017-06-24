import os, codecs, re, csv
from datetime import timedelta
def wordIn(word, phrase):
    return word in phrase.split()


def search(query):
    time=''
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
                    # print(line)
                    break
    return time

def stringToTimedelta(string):
    timeFormats = string.split(':')
    time = 0 + int(timeFormats[2].split(',')[0])
    time += int(timeFormats[1]) * 60
    time += int(timeFormats[0]) * 3600
    return ((timedelta(seconds=time)))


def getScene(query):
    for file in os.listdir('sceneCuts/'):
        with csv.DictReader(file, delimiter=',') as reader:
            timeFormat = search(query)
            timeToSearch = stringToTimedelta(timeFormat)
            for line in reader:
                print(line["first_name"])


getScene('Hey')