#!/bin/env python3

from math import factorial


def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


def binomial_distribution(n,x,p,q):
    return nCr(n,x) * (p**x) * (q**(n-x)) 


def main():
    b,g = map(float, input().split())
    n = 6
    p = b / (b+g)
    q = g / (b+g)

    ans = 0
    for x in range(3,n+1):
        ans += binomial_distribution(n,x,p,q)

    print(round(ans, 3))


if __name__ == '__main__':
    main()