#!/usr/bin/env python3


def main():
	color_dict = { 
		'purple':0,
		'green':1,
		'blue':2,
		'orange':3,
		'red':4,
		'yellow':5
	}
	gems = ['Power','Time','Space','Soul','Reality','Mind']

	gauntlet = [False for _ in range(6)]

	n = int(input())
	
	for _ in range(n):
		stone = str(input())
		gauntlet[color_dict[stone]] = True

	print(6-n)

	for i in range(6):
		if gauntlet[i] == False:
			print(gems[i])



if __name__ == '__main__':
	main()