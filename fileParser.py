def parseText(path):
    parsedText = []
    text = _readFile(path)
    rawParsedText = text.split(" ")

    for i in range(0, len(rawParsedText)):
        currWord = rawParsedText[i]
        if doesWordContainsApostrophe(currWord):
            wordToAdd = []
            if isItRightSingleQuotationMark(currWord):
                wordToAdd = currWord.split(chr(8217))
            elif isItNormalSingleQuote(currWord):
                wordToAdd = currWord.split(chr(39))
            parsedText.append(wordToAdd[0])
            parsedText.append(chr(39))
            parsedText.append(wordToAdd[1])
        elif '.' in currWord:
            parsedText.append(currWord[:-1])
            parsedText.append('.')
        elif ',' in currWord:
            parsedText.append(currWord[:-1])
            parsedText.append(',')
        elif chr(34) in currWord:
            if currWord[0] == chr(34):
                parsedText.append(chr(34))
                parsedText.append(currWord[1:])
            elif currWord[-1] == chr(34):
                parsedText.append(currWord[:-1])
                parsedText.append(chr(34))
        else:
            parsedText.append(currWord)
    return parsedText

def doesWordContainsApostrophe(word):
    return (chr(8217) or chr(39)) in word

def isItRightSingleQuotationMark(word):
    return chr(8217) in word

def isItNormalSingleQuote(word):
    return chr(39) in word

def doesWordContainsDoubleQuotes(word):
    return chr(34) in word

def _readFile(path):
    f = open(path, "r", encoding='utf-8')
    return f.read()