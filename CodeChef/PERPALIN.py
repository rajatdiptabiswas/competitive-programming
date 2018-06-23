#!/usr/bin/env python3

t = int(input())

while(t != 0):
	n,p = map(int, input().split())

	if p == 1 or p == 2:
		print("impossible")

	if p > 2:
		for x in range(n//p):
			for y in range(p):
				if (y == 0):
					print('a', end='')
				elif (y == p-1):
					print('a', end='')
				else:
					print('b', end='')
		print()

	t -= 1