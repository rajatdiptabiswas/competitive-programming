#!/usr/bin/env python3

"""
aabb
aabbaabb
01234567
0:4
1:5
2:6
3:7

aabb
abba *
bbaa
baab *
aabb
"""


def is_palindrome(string):
	if string == string[::-1]:
		return True
	else:
		return False


def double_string(string):
	return string + string


def main():
	t = int(input())

	for testcase in range(t):
		string = str(input())
		length = len(string)

		check = double_string(string)

		count = 0

		for x in range(length):
			if is_palindrome(check[x:length + x]):
				count += 1

		print(count)


if __name__ == '__main__':
	main()
