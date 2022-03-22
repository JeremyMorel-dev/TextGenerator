import fileParser as fp
import sys
sys.path.insert(0, './classes')
from word import Word


print(Word("écrire").getWord())
print(fp.parseText("test.txt"))