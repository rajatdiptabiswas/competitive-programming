#!/bin/env python3

from math import factorial


def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


def binomial_distribution(n,x,p):
    return nCr(n,x) * (p**x) * ((1-p)**(n-x)) 


def main():
    d,n = map(float, input().split())
    d = d/100

    # 0, 1, 2
    ans = 0
    for x in range(3):
        ans += binomial_distribution(n,x,d)

    print(round(ans, 3))

    # 2, 3, 4, 5, ... 10  
    ans = 0
    for x in range(2, 11):
        ans += binomial_distribution(n,x,d)

    print(round(ans, 3))


if __name__ == '__main__':
    main()