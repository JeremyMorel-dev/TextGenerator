import os
import fileParser as fp
from word import Word

class TextEngine:
    _wordList = []

    def __init__(self):
        self._initWordList()

    def _initWordList(self):
        pathList = self._getFilesPathList()
        for path in pathList:
            parsedText = self._readText(path)
            for word in parsedText:
                self._wordList.append(Word(word))
    
    def _readText(self, path):
        return fp.parseText(path)
            
    def _getFilesPathList(self):
        pathList = []
        for filename in os.listdir("src"):
            f = os.path.join("src", filename)
            if os.path.isfile(f):
                pathList.append(f)
        return pathList
    
    def getWordList(self):
        return self._wordList