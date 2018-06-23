#!/usr/bin/env python3


def main():
	t = int(input())

	while (t != 0):
		n = int(input())

		string = ['' for _ in range(n)]

		for x in range(n):
			string[x] = str(input())

		unique = list(set(string))

		team_1 = 0
		team_2 = 0

		for x in range(n):
			if (string[x] == unique[0]):
				team_1 += 1

			elif (string[x] == unique[1]):
				team_2 += 1

		if (team_1 > team_2):
			print(unique[0])
		elif (team_2 > team_1):
			print(unique[1])
		else:
			print("Draw")

		t -= 1


if __name__ == '__main__':
	main()