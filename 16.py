from functools import reduce
from math import gcd

import sys

nums = []

for line in sys.stdin:
    for num in line.split():
        nums.append(int(num))

print(reduce(lambda x, y: gcd(x, y), nums))
