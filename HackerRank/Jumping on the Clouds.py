#!/usr/bin/env python3


def main():
	n = int(input())
	array = [int(x) for x in input().split(' ')]

	zeroes = 0
	ans = 0

	for i in range(n):
		if (array[i] == 1):
			ans += (zeroes//2) + 1
			zeroes = 0
		else:
			zeroes += 1

	if (zeroes > 1):
		ans += zeroes//2

	print(ans)


if __name__ == '__main__':
	main()