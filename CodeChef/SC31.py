#!/usr/bin/env python3

from functools import reduce


def main():
    t = int(input())

    for testcase in range(t):
        n = int(input())

        dec_ints = []

        for _ in range(n):
            bin_string = str(input())
            dec_int = int(bin_string, 2)
            dec_ints.append(dec_int)

        ans = reduce(lambda x,y: x^y, dec_ints)

        print(bin(ans).count('1'))


if __name__ == '__main__':
    main()