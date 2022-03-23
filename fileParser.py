def parseText(fileName):
    parsedText = []
    text = _readFile(fileName)
    rawParsedText = text.split(" ")

    for i in range(0, len(rawParsedText)):
        currWord = rawParsedText[i]
        p = 1
        if (chr(8217) or chr(39)) in currWord:
            wordToAdd = []
            print(chr(8217) in currWord)
            if chr(8217) in currWord:
                wordToAdd = currWord.split(chr(8217))
            elif chr(39) in currWord:
                wordToAdd = currWord.split(chr(39))
            print(wordToAdd)
            parsedText.append(wordToAdd[0])
            parsedText.append(chr(39))
            parsedText.append(wordToAdd[1])
        elif '.' in currWord:
            parsedText.append(currWord[:-1])
            parsedText.append('.')
        elif ',' in currWord:
            parsedText.append(currWord[:-1])
            parsedText.append(',')
        else:
            parsedText.append(currWord)
    return parsedText


def _readFile(fileName):
    f = open("./src/" + fileName, "r", encoding='utf-8')
    return f.read()