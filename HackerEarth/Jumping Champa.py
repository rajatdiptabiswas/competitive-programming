#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		n,q = map(int, input().split())
		a = [int(x) for x in input().split()]
		a.sort()

		total = 0

		for i in range(1, len(a)):
			total += a[i] - a[i-1]

		print(q*total)

if __name__ == '__main__':
	main()