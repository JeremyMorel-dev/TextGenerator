import fileParser as fp
import os
import sys
sys.path.insert(0, './classes')
from word import Word

for filename in os.listdir("src"):
    f = os.path.join("src", filename)
    if os.path.isfile(f):
        print(fp.parseText(f))