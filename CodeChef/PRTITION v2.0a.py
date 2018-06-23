#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		x, n = map(int, input().split())

		summation = ((n * (n + 1)) // 2) - x

		if n == 2 or n == 3 or summation%2 != 0:
			print("impossible")
			continue
		else:
			sets = set()
			req_sum = summation//2

			for e in range(n,1,-1):
				if e == x:
					continue
				
				sets.add(e)
				req_sum -= e

				if req_sum == 0:
					break
				elif req_sum < 0:
					req_sum += e
					sets.remove(e)

			if req_sum > 0:
				print("impossible")
				continue

			# print(sets)
			# print(sum(sets))

			for i in range(1,n+1):
				if i == x:
					print('2', end='')
				elif i in sets:
					print('1', end='')
				elif i not in sets:
					print('0', end='')
			print()


if __name__ == '__main__':
	main()
