#!/usr/bin/env python3

import math


def factors(n):
    factor_list = []
    for i in range(1, math.floor(n**0.5)+1):
        if n % i == 0:
            if i == n//i:
                factor_list.append(i)
            else:
                factor_list.append(i)
                factor_list.append(n//i)
    return sorted(factor_list)


def sieve(n):
    prime_bool = [True for _ in range(n+1)]
    
    for i in range(math.ceil(n**0.5)):
        if i == 0 or i == 1 or not prime_bool:
            prime_bool[i] = False
            continue
        else:
            for p in range(2*i, n+1, i):
                prime_bool[p] = False

    primes = []

    for i in range(n+1):
        if prime_bool[i]:
            primes.append(i)

    return set(primes)


def main():
    n = int(input())

    primes = sieve(n)
#    print(primes)
#
#    for i in range(2, n):
#        print("i = ", i)
#
#        factor = factors(i)
#        print(factor)
#
#        prime_intersect = primes.intersection(set(factor))
#        print(prime_intersect)
#
#        print("x = " + str(len(factor)), end="; ")
#        print("k = " + str(len(prime_intersect)))
#        print()

    xk = [] 

#    x = set()
#    k = set()

    for i in range(2, n):
        factor = factors(i)
        prime_intersect = primes.intersection(set(factor))
        
#        x.add(len(factor))
#        k.add(len(prime_intersect))

        xk.append((len(factor), len(prime_intersect)))
        xk = list(set(xk))
        xk.sort(key=lambda x:x[0])
        xk.sort(key=lambda x:x[1])

#        print(i, '\t', str(len(factor)), '\t', str(len(prime_intersect)))
 
#    print(x)
#    print(k)

#    for x in xk:
#        print(x)

    # printing for testing
    print(len(xk))
    for x in xk:
        print(x[0], x[1])


if __name__ == '__main__':
    main()
