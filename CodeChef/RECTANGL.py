#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		a,b,c,d = map(int, input().split())

		if (a^b^c^d == 0):
			print("YES")
		else:
			print("NO")


if __name__ == '__main__':
	main()