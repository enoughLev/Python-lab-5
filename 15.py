from functools import reduce
import sys

words = []

for line in sys.stdin:
    for word in line.split():
        words.append(str(word))

print(reduce(lambda a, b: a if a < b else b, words))