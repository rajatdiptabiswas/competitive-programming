#!/usr/bin/env python3

import math
import functools
import sys


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
		arr = [int(e) for e in input().split()]	
		rev_arr = list(reversed(arr))

		summation = int(functools.reduce(lambda x,y:x+y, arr))

		if all(a>=0 for a in arr):
			print(summation * k)

		elif all(a<=0 for a in arr):
			print(max(arr))

		else:
			if summation > 0:
				value = summation*(k-2)
				
				forward = 0
				reverse = 0
				forward_max = 0
				reverse_max = 0
				
				for i in range(n):
					forward += int(arr[i])
					if forward >= forward_max:
						forward_max = forward
					
					reverse += int(rev_arr[i])
					if reverse >= reverse_max:
						reverse_max = reverse
					
				value += forward_max + reverse_max
				
				print(value)

			elif int(summation) <= 0:
				if k == 1:
					print(str(maxSubArraySum(arr, len(arr))))
				else:
					arr_times_2 = arr*2
					print(str(maxSubArraySum(arr_times_2, len(arr_times_2))))


if __name__ == '__main__':
	main()