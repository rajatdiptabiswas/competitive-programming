#!/usr/bin/env python3

from itertools import islice


def van_eck():
    n, seen, val = 0, {}, 0
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, 1)
        seen.update(last)
        n += 1


def main():
    seq = list(islice(van_eck(), 130))

    t = int(input())

    for testcase in range(t):
        n = int(input())
        x = seq[n-1]

        print(seq[:n].count(x))


if __name__ == '__main__':
    main()