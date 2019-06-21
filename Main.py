import pandas as pd
import random
line = random.choice(open('output-onlinerandomtools.csv').readlines())
print(line)
finalcount = len(line) - 3
print(finalcount)
