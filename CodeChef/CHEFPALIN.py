#!/usr/bin/env python3

string_az = 'abcdefghijklmnopqrstuvwxyz'
string_special = 'abbaba'

t = int(input())

while(t != 0):
	n,a = map(int, input().split())

	if (a >= n):
		print("1", string_az[0:n])

	elif (a < n):
		if (a == 1):
			print(str(n), end = ' ')
			for i in range(n):
				print(string_az[0], end = '')
			print()

		elif (a == 2):
			if (n < 5):
				print("2", end = ' ')
				
				if (n % 2 == 0): # even
					for i in range(n//2): 
						print(string_az[0], end = '') # print a

				else: # odd
					for i in range(n//2 + 1): 
						print(string_az[0], end = '') # print a
					
				for i in range(n//2): 
					print(string_az[1], end = '') # print b

				print()


			elif (n <= 8 and n >= 5):
				print("3", end = ' ')

				if(n % 2 == 0): # even
					for i in range(n//2 - 1):
						print(string_az[0], end = '') # print a
				else: # odd
					for i in range(n//2): 
						print(string_az[0], end = '') # print a

				print(string_az[1], end = '') # print b
				print(string_az[0], end = '') # print a

				for i in range(n//2 - 1):
					print(string_az[1], end = '') # print b

				print()

			elif (n > 8):
				print("4", end = ' ')

				if (n > len(string_special)):
					print((string_special * (n//len(string_special))), end = '')

				print((string_special[:(n % len(string_special))]))

		elif (a > 2):
			print("1", end = ' ')
			print((string_az[0:a] * (n//a)), end = '')
			print(string_az[0:(n%a)])

	t -= 1