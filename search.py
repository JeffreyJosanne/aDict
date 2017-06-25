import os, codecs, re, csv
from datetime import timedelta


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
                    # print(line)
                    break
    return time


def stringToTimedelta(string):
    timeFormats = string.split(':')
    time = 0 + int(timeFormats[2])
    time += int(timeFormats[1]) * 60
    time += int(timeFormats[0]) * 3600
    return ((timedelta(seconds=time)))


def stringToSeconds(string):
    timeFormats = string.split(':')
    time = 0 + int(timeFormats[2])
    time += int(timeFormats[1]) * 60
    time += int(timeFormats[0]) * 3600
    return time

def stringToSecondsWithComma(string):
    timeFormats = string.split(':')
    time = 0 + int(timeFormats[2].split(',')[0])
    time += int(timeFormats[1]) * 60
    time += int(timeFormats[0]) * 3600
    return time

def getScene(query):
    startTime=timedelta(seconds=0)
    endTime= timedelta(seconds=0)
    timeFormat = search(query)
    timeSeconds = stringToSecondsWithComma(timeFormat)
    print(str(timedelta(seconds=timeSeconds)))
    for file in os.listdir('sceneCuts/'):
        reader = csv.reader(open('sceneCuts/' + file, 'r'))
        for row in reader:
            # print(row)
            if ((int(row[0])> timeSeconds)&((int(row[1])< timeSeconds))):
                # print(str(timedelta(seconds=int(row[0])))+'-->'+str(timedelta(seconds=int(row[1]))))
                startTime = timedelta(seconds=int(row[0]))
                endTime = timedelta(seconds=int(row[1]))
        print(str(startTime)+'-->'+str(endTime))



getScene('make')
