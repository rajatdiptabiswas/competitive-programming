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
		n,k = map(int, input().split(' '))
		arr = [int(e) for e in input().split(' ')]	
		rev_arr = list(reversed(arr))

		summation = int(functools.reduce(lambda x,y:x+y, arr))

		if all(int(a)>=0 for a in arr):
			sys.stdout.write(str(summation * k))

		elif all(int(a)<=0 for a in arr):
			sys.stdout.write(str(max(arr)))

		else:
			if int(summation) > 0:
				value1 = summation*k
				
				value2 = summation*(k-2)
				forward = 0
				i = 0
				while int(arr[i]) > 0:
					forward += int(arr[i])
					i += 1
				value2 += forward
				reverse = 0
				i = 0
				while int(rev_arr[i]) > 0:
					reverse += int(rev_arr[i])
					i += 1
				value2 += reverse

				value = max(value1,value2)
				sys.stdout.write(str(value))

			elif int(summation) <= 0:
				if k == 1:
					sys.stdout.write(str(maxSubArraySum(arr, len(arr))))
				else:
					arr_times_2 = arr*2
					sys.stdout.write(str(maxSubArraySum(arr_times_2, len(arr_times_2))))

		sys.stdout.write("\n")


if __name__ == '__main__':
	main()