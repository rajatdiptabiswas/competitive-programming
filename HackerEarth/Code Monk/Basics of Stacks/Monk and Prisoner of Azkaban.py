#!/usr/bin/env python3

"""
find largest index x less than index i
such that value at x > value at i

find smallest index y greater than index i
such that value at y > value at i
"""

# CONSTANTS
INDEX = 0
VALUE = 1

stack = []


def find_next_greater(input, output):
	for i in range(len(input)):
		if i == 0:
			stack.append(input[i])
		else:
			if len(stack) != 0:
				top = stack.pop()

				while input[i][VALUE] > top[VALUE]:
					output[top[INDEX]] = i + 1

					if len(stack) == 0:
						break

					top = stack.pop()

				if input[i][VALUE] <= top[VALUE]:
					stack.append(top)

			stack.append(input[i])

	while len(stack) != 0:
		top = stack.pop()
		output[top[INDEX]] = -1


def main():
	n = int(input())
	a_input = [int(x) for x in input().split()]
	# a_input = [5,4,1,3,2]
	# n = len(a_input)
	a = [(i, a_input[i]) for i in range(n)]
	rev_a = a[::-1]

	next_greater = [0 for x in range(n)]
	prev_greater = [0 for y in range(n)]

	find_next_greater(a, next_greater)
	find_next_greater(rev_a, prev_greater)

	for i in range(n):
		if prev_greater[i] != -1:
			prev_greater[i] = n - prev_greater[i] + 1

	# print(next_greater)
	# print(prev_greater)

	ans = [next_greater[i]+prev_greater[i] for i in range(n)]

	for item in ans:
		print(item, end=' ')


if __name__ == '__main__':
	main()
