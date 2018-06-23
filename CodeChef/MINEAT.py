#!/usr/bin/env python3


def time_taken(arr, k):
	time = 0

	for i in arr:
		if i <= k:
			time += 1
		else:
			if i % k == 0:
				time += i // k
			else:
				time += i // k + 1

	return time


def search_k(left, right, arr, hrs):
	mid = left + (right - left) // 2
	time = time_taken(arr, mid)

	if left == right:
		return mid

	if time <= hrs:  # left
		return search_k(left, mid, arr, hrs)

	elif time > hrs:  # right
		return search_k(mid + 1, right, arr, hrs)


def main():
	t = int(input())

	for testcase in range(t):
		n, hours = map(int, input().split())
		banana = [int(x) for x in input().split()]
		banana.sort()

		l = 1
		r = max(banana)

		print(search_k(l, r, banana, hours))


if __name__ == '__main__':
	main()
