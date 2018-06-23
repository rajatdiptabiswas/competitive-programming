#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		n,x = map(int, input().split())
		notes = [int(x) for x in input().split()]

		s = sum(notes)
		m = min(notes)

		if (s%x >= m):
			print('-1')
		else:
			print(s//x)


if __name__ == '__main__':
	main()