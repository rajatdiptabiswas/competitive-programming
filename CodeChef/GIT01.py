"""
Equations -> 5a+3b and 5x+3y
a b -> RGRG
x y -> GRGR

R->G (5) (x,a)
G->R (3) (y,b)
"""

#!/usr/bin/env python3


def main():
	t = int(input())

	while (t != 0):
		n, m = map(int, input().split(' '))

		# initialising variables
		string = [['' for i in range(m)] for j in range(n)]
		x = 0
		y = 0
		a = 0
		b = 0

		for i in range(n):
			string[i] = input()

			if (i % 2 == 0): # if on even row
				for j in range(m):
					if (j % 2 == 0): # even position
						if (string[i][j] == 'R'): # R->G (5)
							a += 1 
						elif (string[i][j] == 'G'): # G->R (3)
							y += 1
					else: # odd position
						if (string[i][j] == 'G'): # G->R (3)
							b += 1 
						elif (string[i][j] == 'R'): # R->G (5)
							x += 1
			else: # if on odd row
				for j in range(m):
					if (j % 2 != 0): # odd position
						if (string[i][j] == 'R'): # R->G (5)
							a += 1 
						elif (string[i][j] == 'G'): # G->R (3)
							y += 1
					else: # even position
						if (string[i][j] == 'G'): # G->R (3)
							b += 1 
						elif (string[i][j] == 'R'): # R->G (5)
							x += 1

		# print('x = {}; y = {}; a = {}; b = {}'.format(x, y, a, b))

		if (a < x):
			ans = (5 * a) + (3 * b)
		else:
			ans = (5 * x) + (3 * y)

		print(ans)

		t -= 1


if __name__ == '__main__':
	main()