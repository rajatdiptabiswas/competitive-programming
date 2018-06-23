#!/usr/bin/env python3

from itertools import permutations


def main():
	chef = [''.join(x) for x in permutations('chef')]

	t = int(input())

	for testcase in range(t):
		string = str(input())
		flag = 0
		count = 0

		for i in range(4,len(string)+1):
			if string[i-4:i] in chef:
				flag = 1
				count += 1

		if flag == 1:
			print("lovely {}".format(count))
		else:
			print("normal")


if __name__ == '__main__':
	main()