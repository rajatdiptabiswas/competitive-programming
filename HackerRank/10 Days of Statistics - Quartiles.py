#!/usr/bin/env python3


def median(array):
	n = len(array)

	if n % 2 == 0:
		return (array[n//2-1] + array[n//2])/2
	else:
		return array[n//2]


def printWholeNumber(number):
	string = str(number)
	print(string.rstrip('0').rstrip('.') if '.' in string else string)


def main():
	n = int(input())
	array = sorted([int(x) for x in input().split()])

	if not n % 2 == 0:
		left = array[:n//2]
		right = array[n//2+1:]
	else:
		left = array[:n//2]
		right = array[n//2:]

	printWholeNumber(median(left))
	printWholeNumber(median(array))
	printWholeNumber(median(right))	


if __name__ == '__main__':
	main()