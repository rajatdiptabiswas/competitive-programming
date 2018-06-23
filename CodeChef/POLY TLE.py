#!/usr/bin/env python3

T = int(input())

while (T != 0):
	n = int(input())

	array = [[0]*4 for i in range(n)]

	for x in range(n):
		array[x] = [int(i) for i in input().split()]
		
	q = int(input())

	while (q != 0):
		t = int(input())

		add = [ (array[x][0] + array[x][1] * t + array[x][2] * t**2 + array[x][3] * t**3) for x in range(n) ]

		min_index = add.index(min(add))

		print(add[min_index])

		q -= 1

	T -= 1