#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		tolls = int(input())
		toll_time = [int(toll) for toll in input().split()]
		cars,distance,velocity = map(int, input().split())

		if cars == 2:
			print("{:.8f}".format(max(toll_time)))
		elif cars > 2:
			print("{:.8f}".format(max(toll_time) * (cars-1)))


if __name__ == '__main__':
	main()