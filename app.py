import sys
sys.path.insert(0, './classes')
from textEngine import TextEngine
def main():
    engine = TextEngine()
    for word in engine.getWordList():
        print(word.getWord() + " " + str(word.getAppearanceAvg()) + "%")

main()