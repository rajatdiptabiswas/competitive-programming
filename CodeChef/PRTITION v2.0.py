#!/usr/bin/env python3

import sys


def main():
	t = int(input())

	for testcase in range(t):
		x, n = map(int, input().split())

		summation = ((n * (n + 1)) // 2) - x

		if n == 2 or n == 3 or summation%2 != 0:
			print("impossible")
		else:
			sets = set()
			req_sum = summation//2

			for e in range(n,1,-1):
				if e == x:
					continue
				elif e <= req_sum:
					req_sum -= e
					sets.add(e)
					if req_sum == 0:
						break
				elif e > req_sum:
					continue

			print(sets)
			print(sum(sets))

			for i in range(1,n+1):
				if i == x:
					sys.stdout.write('2')
				elif i in sets:
					sys.stdout.write('1')
				elif i not in sets:
					sys.stdout.write('0')
			sys.stdout.write('\n')


if __name__ == '__main__':
	main()
