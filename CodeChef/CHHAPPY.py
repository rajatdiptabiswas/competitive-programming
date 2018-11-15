#!/usr/bin/env python3
#https://www.codechef.com/NOV18B/problems/CHHAPPY

'''
Example Input
4
4
1 1 2 3
4
2 1 3 3
5
5 4 4 3 1
5
3 2 1 1 4

Example Output
Truly Happy
Poor Chef
Poor Chef
Truly Happy
'''


def main():
	t = int(input())

	for testcase in range(t):
		n = int(input())
		arr = [int(x) for x in input().split()]

		arr_set = list(set(arr))

		elements = [arr[a-1] for a in arr_set if a-1 < len(arr)]

		if len(elements) != len(set(elements)):  # no repeating elements
			print('Truly Happy')
		else:  # repeating elements
			print('Poor Chef')


if __name__ == '__main__':
	main()