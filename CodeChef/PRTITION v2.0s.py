#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		x, n = map(int, input().split())

		summation = ((n * (n + 1)) // 2) - x

		if n == 2 or n == 3 or (summation%2) != 0:
			print("impossible")
			continue
		
		sets = set()
		req_sum = summation//2

		for e in range(n,1,-1):
			if e == x:
				continue
			
			sets.add(e)
			req_sum -= e

			if req_sum == 0:
				break
			elif req_sum < 0 or req_sum == x:
				sets.remove(e)
				req_sum += e		

		if req_sum != 0:
			print("impossible")

		# print(sets)
		# print(sum(sets))

		if req_sum == 0:
			for i in range(1,n+1):
				if i == x:
					print('2', end='')
				elif i in sets:
					print('1', end='')
				elif i not in sets:
					print('0', end='')
			print("")


if __name__ == '__main__':
	main()
