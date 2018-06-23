#!/usr/bin/env python3

from functools import reduce


def main():
	t = int(input())

	for testcase in range(t):
		problems = [0 for i in range(5)]
		n = int(input())

		for i in range(n):
			string = str(input())

			if string == "cakewalk":
				problems[0] += 1
			
			elif string == "simple":
				problems[1] += 1

			elif string == "easy":
				problems[2] += 1

			elif string == "easy-medium" or string == "medium":
				problems[3] += 1
			
			elif string == "medium-hard" or string == "hard":
				problems[4] += 1

		
		possible = reduce(lambda x,y: x >= 1 and y >= 1, problems)

		if possible:
			print("Yes")
		else:
			print("No")


if __name__ == '__main__':
	main()