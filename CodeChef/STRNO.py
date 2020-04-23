#!/usr/bin/env python3

import math


def prime_factors_count(x):
    total = 0
    
    count = 0
    while x % 2 == 0:
        x >>= 1
        count += 1
    
    if count > 0:
        total += count
        # print(2, count)

    for i in range(3, int(math.sqrt(x))+1, 2):
        count = 0
        while x % i == 0:
            count += 1
            x = int(x / i)

        if count > 0:
            total += count
            # print(i, count)

    if x > 2:
        total += 1
        # print(x, 1)

    return total


def main():
    t = int(input())

    for testcase in range(t):
        x, k = map(int, input().split())
        if k <= prime_factors_count(x):
            print(1)
        else:
            # print(x, k)
            print(0)


if __name__ == '__main__':
    main()
