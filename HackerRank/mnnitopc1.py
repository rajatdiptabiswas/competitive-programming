#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		start = [int(x) for x in input().split()]
		finish = [int(y) for y in input().split()]
		a,b = map(int, input().split())

		time_diff = finish[0]*60 + finish[1]
		time_diff -= start[0]*60 + start[1]

		time = 0
		i = 0

		while (time <= time_diff):
			time += a+(i*b)
			i += 1

		print(i-1)


if __name__ == '__main__':
	main()