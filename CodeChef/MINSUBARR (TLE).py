#!/usr/bin/env python3

from itertools import accumulate
import math


def main():
	q = int(input())

	for queries in range(q):
		n, d = map(int, input().split(' '))
		a = [int(x) for x in input().split(' ')]

		prefix = list(accumulate(a, lambda x,y: x+y))
		min_sub = math.inf

		for i in range(n):
			for j in range(i+1, n):
				if prefix[j] - prefix[i] >= d:
					if min_sub > j-i:
						min_sub = j-i
					break

		print(min_sub)


if __name__ == '__main__':
	main()