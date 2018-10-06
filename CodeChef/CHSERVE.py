#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		p1,p2,k = map(int, input().split())
		
		val = (p1+p2)//k

		if (val & 1) == 1:
			print('COOK')
		else:
			print('CHEF')


if __name__ == '__main__':
	main()