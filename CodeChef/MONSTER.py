#!/usr/bin/env python3


def main():
	n = int(input())
	monster = [int(m) for m in input().split()]

	q = int(input())
	for testcase in range(q):
		x,y = map(int, input().split())
		
		for k in range(n):
			if (k & x) == k:
				monster[k] -= y
		
		monsters = n
		for mon in monster:
			if mon <= 0:
				monsters -= 1;

		print(monsters)


if __name__ == '__main__':
	main()