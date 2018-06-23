#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		patents,months,worker_max,workers = map(int, input().split())
		string = str(input())

		if months == 0:
			print('no')
			continue

		even = 0
		odd = 0
		for char in string:
			if char == 'E':
				even += 1
			elif char == 'O':
				odd += 1

		for m in range(1,months+1):
			if m % 2 == 0:
				current_worker = min(worker_max,even)
				even -= current_worker
			else:
				current_worker = min(worker_max,odd)
				odd -= current_worker

			patents -= current_worker

		if patents <= 0:
			print("yes")
		else:
			print("no")


if __name__ == '__main__':
	main()