class Word:

    _prevWordsAvg = dict()
    _nextWordAvg = dict()
    
    def __init__(self, word):
        self._word = word

    def getWord(self):
        return self._word
    
    def getPrevWordAvg(self):
        return self._prevWordsAvg

    def getNextWordAvg(self):
        return self._nextWordsAvg