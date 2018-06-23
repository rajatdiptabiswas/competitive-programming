#!/usr/bin/env python3


def main():
	n, q = map(int, input().split())
	# a = [int(x) for x in input().split()]
	# binary = ['{:031b}'.format(i) for i in a]
	binary = ['{:031b}'.format(int(i)) for i in input().split()]

	zero = [[0 for i in range(n)] for j in range(31)]
	one = [[0 for i in range(n)] for j in range(31)]

	for pos in range(31):
		ones = 0
		zeroes = 0
		item_index = 0

		for item in binary:
			if item[pos] == '0':
				zeroes += 1

			elif item[pos] == '1':
				ones += 1

			zero[pos][item_index] = zeroes
			one[pos][item_index] = ones
			
			item_index += 1

	for queries in range(q):
		l, r = map(int, input().split())
		ans = ''

		for pos in range(31):
			if l == 1:
				ones = one[pos][r - 1]
				zeroes = zero[pos][r - 1]
			else:
				ones = one[pos][r - 1] - one[pos][l - 2]
				zeroes = zero[pos][r - 1] - zero[pos][l - 2]

			if ones < zeroes:
				ans = ans + '1'
			elif ones >= zeroes:
				ans = ans + '0'

		print(int(ans, 2))


if __name__ == '__main__':
	main()
