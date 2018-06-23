#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		g = int(input())
		
		for games in range(g):
			i,n,q = map(int, input().split())

			if n % 2 == 0:
				h = n//2
				t = n//2

			else:
				h = n//2
				t = n//2

				if i == 1:
					t += 1

				elif i == 2:
					h += 1

			if q == 1:
				print(h)
			elif q == 2:
				print(t)


if __name__ == '__main__':
	main()