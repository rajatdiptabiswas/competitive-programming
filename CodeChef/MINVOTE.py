#!/usr/bin/env python3

from itertools import accumulate


def sum_in_between(i, j, prefix):
	l = min(i, j)
	r = max(i, j)

	return prefix[r-1] - prefix[l]


def search_left(left, right, index, array, prefix):
	mid = (left + right) // 2

	if right == left:
		return right

	if right == left + 1:
		if sum_in_between(right, index, prefix) <= array[index]:
			if sum_in_between(left, index, prefix) <= array[index]:
				return left
			else:
				return right

	if sum_in_between(index, mid, prefix) <= array[index]:
		return search_left(left, mid, index, array, prefix)

	else:
		return search_left(mid + 1, right, index, array, prefix)


def search_right(left, right, index, array, prefix):
	mid = (left + right) // 2

	if left == right:
		return left

	if left == right - 1:
		if sum_in_between(index, left, prefix) <= array[index]:
			if sum_in_between(index, right, prefix) <= array[index]:
				return right
			else:
				return left

	if sum_in_between(index, mid, prefix) <= array[index]:
		return search_right(mid, right, index, array, prefix)

	else:
		return search_right(left, mid - 1, index, array, prefix)


def main():
	t = int(input())

	for testcase in range(t):
		n = int(input())
		power = [int(x) for x in input().split()]
		power_prefix = list(accumulate(power, lambda x, y: x + y))
		ans = [0 for a in range(n)]

		for i in range(n):
			if i - 1 >= 0:
				l = search_left(0, i-1, i, power, power_prefix)
			else:
				l = -1

			if i + 1 < n:
				r = search_right(i+1, n-1, i, power, power_prefix)
			else:
				r = -1

			if l != -1:
				for x in range(l, i):
					ans[x] += 1

			if r != -1:
				for x in range(i + 1, r + 1):
					ans[x] += 1

		for val in ans:
			print(val, end=' ')
		print()


if __name__ == '__main__':
	main()
