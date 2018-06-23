#!/usr/bin/env python3


def main():
	n, q = map(int, input().split())
	# a = [int(x) for x in input().split()]
	# binary = ['{:031b}'.format(i) for i in a]
	binary = ['{:031b}'.format(int(i)) for i in input().split()]

	# [0, 1]
	dp = [[[0, 0] for i in range(n)] for j in range(31)]

	for pos in range(31):
		ones = 0
		zeroes = 0
		item_index = 0

		for item in binary:
			if item[pos] == '0':
				zeroes += 1

			elif item[pos] == '1':
				ones += 1

			dp[pos][item_index][0] = zeroes
			dp[pos][item_index][1] = ones
			item_index += 1

	for queries in range(q):
		l, r = map(int, input().split())
		ans = ''

		for pos in range(31):
			if l == 1:
				ones = dp[pos][r - 1][1]
				zeroes = dp[pos][r - 1][0]
			else:
				ones = dp[pos][r - 1][1] - dp[pos][l - 2][1]
				zeroes = dp[pos][r - 1][0] - dp[pos][l - 2][0]

			if ones < zeroes:
				ans = ans + '1'
			elif ones >= zeroes:
				ans = ans + '0'

		print(int(ans, 2))


if __name__ == '__main__':
	main()
