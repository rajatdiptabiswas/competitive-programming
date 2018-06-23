#!/usr/bin/env python3
from functools import reduce


def main():
	n,k = map(int,input().split())
	arr = [int(x) for x in input().split()]
	
	f = []
	
	for l in range(n):
		for r in range(l,n):
			sub = []

			for i in range(l,r+1):
				sub.append(arr[i])

			# print(sub)

			xor_fun = reduce(lambda x,y: x^y, sub)
			min_fun = min(sub)
			
			f.append(xor_fun * min_fun)
	
	# print(f)		
	f_sort = sorted(f)
	# print(f_sort)
	print(f_sort[k-1])
			

if __name__ == '__main__':
	main()