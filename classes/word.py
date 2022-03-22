class Word:

    _prevWordsAvg = dict()
    _nextWordAvg = dict()
    
    def __init__(self, word):
        self._word = word

    def getWord(self):
        return self._word
    
    def getPrevWordAvg(sef):
        return self._prevWordsAvg

    def getNextWordAvg(sef):
        return self._nextWordsAvg