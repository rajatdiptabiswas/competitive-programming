#!/usr/bin/env python3

from random import randint 


def gen_helper(n, m, k, w_min, w_max):
    v = [[0 for x in range(m)] for y in range(k)]

    for i in range(1,k+1):
        for j in range(1,m+1):
            v[i-1][j-1] = randint(w_min, w_max)

    for x in v:
        print(x)
    print()

    for k in v:
        for m in k:
            print(m/sum(k), end=',')
        print()
    print()


def print_gen(t, n, m, k):
    print(t)
    print(n, m, k)
    for i in range(n):
        for j in range(k):
            print(randint(1,m), end=' ')
        print()


def group(no):
    params = [
        [10, 4, 25, 10, 20],
        [100, 2, 1000, 1, 1],
        [100, 4, 1000, 45, 55],
        [200, 2, 5000, 1, 5],
        [300, 4, 3000, 1, 100],
        [500, 9, 2000, 20, 80]
    ]
    return params[no]


if __name__ == '__main__':
    t = int(input())

    # for test in range(t):
        # item = [int(x) for x in input('n, m , k, w_min, w_max\n').split()]
        # gen(*item)

    print_gen(t, *group(0)[:3])
