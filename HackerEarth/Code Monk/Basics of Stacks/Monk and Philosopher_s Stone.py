#!/usr/bin/env python3

from functools import reduce

stack = []

def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	q,x = map(int, input().split(' '))

	i = 0

	for _ in range(q):
		string = str(input())

		if string == 'Harry':
			stack.append(a[i])
			i += 1

		elif string == 'Remove':
			stack.pop()

		if reduce(lambda x,y: x+y, stack) == x:
			print(len(stack))
			return

	print(-1)


if __name__ == '__main__':
	main()