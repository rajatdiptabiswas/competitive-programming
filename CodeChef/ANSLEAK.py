#!/usr/bin/env python3

from collections import Counter


def main():
    t = int(input())
    n, m, k = map(int, input().split())
    for test in range(t):
        for i in range(n):
            k = [int(x) for x in input().split()]
            print(Counter(k).most_common(1)[0][0], end = ' ')
        print()


if __name__ == '__main__':
    main()
