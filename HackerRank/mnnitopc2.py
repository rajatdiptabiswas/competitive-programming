#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		n,m = map(int, input().split())

		x = int((2*m)**(1/2))

		while x*(x + 1) <= 2*m:
			x += 1

		print(m - ((x*(x-1))//2))


if __name__ == '__main__':
	main()