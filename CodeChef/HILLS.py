#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		n, u, d = map(int, input().split())
		a = [int(x) for x in input().split()]

		i = 0
		special = True

		while (i < n-1):
			if a[i] - d <= a[i+1] <= a[i] + u:
				i += 1
				continue

			elif a[i + 1] < a[i] and special:
				special = False
				i += 1
				continue

			else:
				break

		print(i+1)


if __name__ == '__main__':
	main()