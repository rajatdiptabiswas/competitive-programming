#!/usr/bin/env python3

t = int(input())
mod = 1000000007

while(t != 0):
	a = int(input())
	t -= 1

	if(a == 0):
		print('1')
		continue

	elif(a == 1):
		print('2')
		continue

	i = 3
	j = 2
	for x in range(2, a):
		i = i % mod
		j = j % mod
		temp = i
		i = i + j
		j = temp

	print(i+j)
	continue
		