class Word:

    _prevWordsAvg = dict()
    _nextWordAvg = dict()
    _wordCount = 0
    _appearanceAvg = 0
    
    def __init__(self, word):
        self._word = word

    def getWord(self):
        return self._word
    
    def getPrevWordAvg(self):
        return self._prevWordsAvg

    def getNextWordAvg(self):
        return self._nextWordsAvg
    
    def getWordCount(self):
        return self._wordCount
    
    def getAppearanceAvg(self):
        return self._appearanceAvg
    
    def incrWordCount(self):
        self._wordCount += 1

    def setAppearanceAvg(self, appearanceAvg):
        self._appearanceAvg = appearanceAvg
    
    