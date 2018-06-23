#!/usr/bin/env python3


def main():
	t = int(input())
	
	for testcases in range(t):
		n = int(input())	
		a = [int(x) for x in input().split()]
		
		odd = 0
		even = 0
		
		for e in a:
			if e%2 != 0:
				odd += 1
			else:
				even += 1
								
		if odd < 2 and even < 2:
			print(n)
			continue
		else:
			while (odd >= 2):
				n -= 1
				odd -= 2
				even += 1
				
			while (even >= 2):
				n -= 1
				even -= 1
				
			print(n)
			continue
	

if __name__ == '__main__':
	main()