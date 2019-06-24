import pandas as pd
import random
import time

# taking the attempts
attempts = input('Enter the attempts you want [1-6] : ')
print('Number of Attempts : ' + attempts)
print('Selecting a Number....')
time.sleep(1)

# selecting a word
line = random.choice(open('output-onlinerandomtools.csv').readlines())
# print(line)

# printing the count
finalcount = len(line) - 3
print(finalcount)

# printingstar = line-3

finalfinal = str(finalcount)
for i in range(finalcount):
    print('*', end=" ")

print('')
