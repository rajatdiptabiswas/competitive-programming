#!/usr/bin/env python3

from random import randint
import sys

t = int(sys.argv[1])

print(t)

for i in range(t):
    # 1 <= n <= 10**5
    # |a| <= 10**9
    n = randint(1, 100)
    print(n)
    for x in range(n):
        print(randint(-1000, 1000), end=" ")
    print()
