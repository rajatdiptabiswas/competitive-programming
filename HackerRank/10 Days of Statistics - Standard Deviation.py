#!/usr/bin/env python3


def main():
	n = int(input())
	array = [int(x) for x in input().split()]

	mean = sum(array)/len(array)

	total = 0

	for i in array:
		total += (i - mean)**2

	sd = (total/n)**0.5

	print(round(sd,1))


if __name__ == '__main__':
	main()