#!/usr/bin/env python3

from functools import reduce


def main():
    t = int(input())
    
    while (t != 0):
        array = [int(x) for x in input().split()]

        print(reduce(lambda x,y : x^y, array))
        
        t -= 1


if __name__ == '__main__':
	main()