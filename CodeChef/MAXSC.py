#!/usr/bin/env python3


def main():
	def max_less_than_target(list, target):
		if target not in list:
			list.append(target)
		list.sort()
		return list[list.index(target) - 1]

	q = int(input())

	for queries in range(q):
		n = int(input())

		array = [[0 for x in range(n)] for y in range(n)]

		for i in range(n):
			array[i] = [int(e) for e in input().split()]

		summation = 0
		flag = 1
		target = max(array[n-1])
		summation += target

		n -= 2

		while n >= 0:
			num = max_less_than_target(array[n], target)

			if num < target:
				summation += num
				target = num

			else:
				print('-1')
				flag = 0
				break

			n -= 1

		if flag != 0:
			print(summation)


if __name__ == '__main__':
	main()
