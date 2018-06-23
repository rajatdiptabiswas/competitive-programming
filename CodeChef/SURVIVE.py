#!/usr/bin/env python3

import math

def main():
	t = int(input())

	for testcase in range(t):
		n,k,s = map(int, input().split())

		work_days = s - (s//7)
		total_consumption = k*s

		if (n*work_days < total_consumption):
			print(-1)

		else:
			print(math.ceil(total_consumption/n))


if __name__ == '__main__':
	main()