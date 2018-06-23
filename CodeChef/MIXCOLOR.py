#!/usr/bin/env python3

from collections import Counter


def main():
	t = int(input())

	for testcase in range(t):
		n = int(input())
		a = [int(x) for x in input().split()]
		freq = Counter(a)

		ans = 0

		for key, num in freq.items():
			if num > 1:
				ans += num-1

		print(ans)


if __name__ == '__main__':
	main()