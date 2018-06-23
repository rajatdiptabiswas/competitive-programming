#!/usr/bin/env python3


def main():
	q = int(input())

	for queries in range(q):
		n, day = map(str, input().split())
		n = int(n)
		extra = n - 28

		week = [4 for a in range(7)]

		if extra > 0:

			if day == 'mon':
				start = 0

			elif day == 'tues':
				start = 1

			elif day == 'wed':
				start = 2

			elif day == 'thurs':
				start = 3

			elif day == 'fri':
				start = 4

			elif day == 'sat':
				start = 5

			elif day == 'sun':
				start = 6

			for i in range(extra):
				i += start

				week[i % 7] += 1

		for w in range(7):
			print(week[w], end=' ')
		print()


if __name__ == '__main__':
	main()