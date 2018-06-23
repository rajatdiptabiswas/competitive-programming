#!/usr/bin/env python3

import math

t = int(input())

while(t != 0):
	n,r = map(int, input().split())
	pre = [int(n) for n in input().split()]

	low = -1 * math.inf
	high = math.inf

	flag = True

	for x in range(n):
		if (pre[x] > low and pre[x] < high):
			if (pre[x] > r):
				high = pre[x]
			elif (pre[x] < r):
				low = pre[x]

		else:
			flag = False

	if flag:
		print("YES")
	else:
		print("NO")


	t -= 1