import os
import fileParser as fp
from word import Word

class TextEngine:
    _wordList = []
    _totalWordCount = 0

    def __init__(self):
        self._initWordList()

    def _initWordList(self):
        pathList = self._getFilesPathList()
        for path in pathList:
            parsedText = self._readText(path)
            self._totalWordCount += len(parsedText)
            for rawWord in parsedText:
                currRawWord = rawWord.lower()
                if not self._wordList:
                    self._wordList.append(Word(currRawWord))
                else:
                    wordFound = 0
                    for word in self._wordList:
                        if word.getWord() == currRawWord:
                            wordFound = 1
                            word.incrWordCount()
                            break
                    if wordFound != 1:
                        self._wordList.append(Word(currRawWord))
        self._calculateEachWordAvgAppearance()

    
    def _calculateEachWordAvgAppearance(self):
        for word in self._wordList:
            word.setAppearanceAvg(round((word.getWordCount() / self._totalWordCount)*100,2))            

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

    def getTotalWordCount(self):
        return self._totalWordCount