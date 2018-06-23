#!/usr/bin/env python3


def main():
	n = int(input())
	bread = [int(x) for x in input().split()]
	even = [0 for i in range(n)]
	sum_even = 0

	for i in range(n):
		even[i] = bread[i] % 2
		sum_even += even[i]

	found_1 = False
	zeroes = 0
	ans = 0

	if sum_even % 2 == 0:
		for i in range(n):
			if even[i] == 0 and found_1 == False:  # 00
				pass

			elif even[i] == 0 and found_1 == True:  # 01
				zeroes += 1

			elif even[i] == 1 and found_1 == False:  # 10
				zeroes = 0
				found_1 = True

			elif even[i] == 1 and found_1 == True:  # 11
				ans += 2 * (zeroes + 1)
				zeroes = 0
				found_1 = False

		print(ans)

	else:
		print("NO")


if __name__ == '__main__':
	main()