#!/usr/bin/env python3


def main():
	n, q = map(int, input().split())
	a = [int(x) for x in input().split()]
	binary = ['{:031b}'.format(i) for i in a]

	for queries in range(q):
		l, r = map(int, input().split())

		ans = ''

		for pos in range(31):
			ones = 0
			zeroes = 0

			for item in binary[l - 1:r]:
				if item[pos] == '0':
					zeroes += 1
				elif item[pos] == '1':
					ones += 1

			if ones < zeroes:
				ans = ans + '1'
			elif ones >= zeroes:
				ans = ans + '0'

		print(int(ans, 2))


if __name__ == '__main__':
	main()