#!/usr/bin/env python3

from math import cos,acos
from fractions import Fraction,gcd
MOD = 1000000007


# Function to find modular inverse of a under modulo m
# Assumption: m is prime
def modInverse(a, m) :
    g = gcd(a, m)
     
    if (g != 1) :
        print("Inverse doesn't exist")
         
    else :   
        # If a and m are relatively prime,
        # then modulo inverse is a^(m-2) mode m
        return (power(a, m - 2, m))

     
# To compute x^y under modulo m
def power(x, y, m) :
     
    if (y == 0) :
        return 1
         
    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0) :
        return p 
    else : 
        return ((x * p) % m)


def main():
	t = int(input())

	for testcase in range(t):
		length,distance_x,time = map(int, input().split())

		ans = length*cos(acos(distance_x/length)*time)
		ans_fraction = Fraction(ans).limit_denominator()
		p = ans_fraction.numerator
		q = ans_fraction.denominator
		r = modInverse(q, MOD)

		# debug
		print("ans = {}; fraction = {}; r = {}".format(ans, ans_fraction, r))

		print((p*r)%MOD)


if __name__ == '__main__':
	main()