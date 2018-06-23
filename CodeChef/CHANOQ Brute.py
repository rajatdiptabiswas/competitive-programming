#!/usr/bin/env python3


def main():
	t = int(input())

	for testcase in range(t):
		segments = int(input())

		lr_input = []
		for i in range(segments):
			lr = [int(x) for x in input().split()]
			lr_input.append(lr)

		query = int(input())

		for q in range(query):
			queries = [int(x) for x in input().split()]
			queries.pop(0)

			count = 0
			good = 0
			for i in range(segments):
				for item in queries:
					if lr_input[i][0] <= item <= lr_input[i][1]:
						count += 1

				if count % 2 != 0:
					good += 1

				count = 0

			print(good)


if __name__ == '__main__':
	main()