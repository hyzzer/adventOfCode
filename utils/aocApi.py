import requests
from os import path

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))

def getPuzzleInput(year, exerciceNumber, url='', sessionCookie=''):
    if url == '':
        url = "https://adventofcode.com/{}/day/{}/input".format(year, exerciceNumber)
        
    if sessionCookie == '':
        with open("{}/.session-cookie".format(ROOT_DIR)) as cookieFile:
            sessionCookie = cookieFile.readline()

    parameters = {
        'session' : sessionCookie
    }

    return requests.get(url.format(exerciceNumber), cookies=parameters).content.decode('utf-8')

def getPuzzleInputFromFile(year, exerciceNumber, inputFilename=None):
    
    if not inputFilename:
        inputFilename = "{}/{}/inputs/chall{}.txt".format(ROOT_DIR, year, exerciceNumber)
        
        if not path.exists(inputFilename):
            with open(inputFilename, 'w+') as inputFile:
                inputFile.write(getPuzzleInput(year, exerciceNumber))

    with open(inputFilename) as inputFile:
        return inputFile.read()
        
            