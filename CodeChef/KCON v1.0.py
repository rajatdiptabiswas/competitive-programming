#!/usr/bin/env python3

import math


def maxSubArraySum(a,size):
      
    max_so_far = -math.inf
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far


def main():
	t = int(input())

	for testcase in range(t):
		n,k = map(int, input().split())
		arr = [int(x) for x in input().split()]	
		array = arr * k
		
		print(maxSubArraySum(array,len(array)))
		

if __name__ == '__main__':
	main()