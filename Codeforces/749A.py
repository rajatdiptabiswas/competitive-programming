#!/usr/bin/env python3


def main():
	n = int(input())

	if n%2 != 0:
		x = (n-3)//2

		print(n//2)
		
		for i in range(x):
			print(2, end=' ')
		print(3, end=' ')
		print()

	else:
		x = n//2

		print(x)
	
		for i in range(x):
			print(2, end=' ')
		print()


if __name__ == '__main__':
	main()