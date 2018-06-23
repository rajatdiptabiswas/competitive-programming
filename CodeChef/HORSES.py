#!/usr/bin/env python3

import math


def main():
	t = int(input())

	while (t != 0):
		n = int(input())

		array = [int(x) for x in input().split()]
		array = sorted(array)

		diff = math.inf

		for i in range(1, n):
			if (abs(array[i] - array[i-1]) < diff):
				diff = abs(array[i] - array[i-1])

		print(diff)

		t -= 1


if __name__ == '__main__':
	main()