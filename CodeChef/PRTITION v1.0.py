#!/usr/bin/env python3

import sys


def main():
	t = int(input())

	for testcase in range(t):
		x, n = map(int, input().split())
		elements = {i for i in range(1, n + 1) if i != x}

		summation = ((n * (n + 1)) // 2)

		if x <= n:
			summation -= x

		if summation % 2 != 0 or n == 2 or n == 3:
			print("impossible")
		else:
			set_1 = set()
			set_2 = set()

			for e in sorted(elements, reverse=True):
				if sum(set_1) < sum(set_2):
					set_1.add(e)
				else:
					set_2.add(e)

			# print(set_1)
			# print(sum(i for i in set_1))
			# print(set_2)
			# print(sum(i for i in set_2))

			for i in range(1,n+1):
				if i == x:
					sys.stdout.write('2')
				elif i in set_1:
					sys.stdout.write('0')
				elif i in set_2:
					sys.stdout.write('1')
			sys.stdout.write('\n')


if __name__ == '__main__':
	main()
