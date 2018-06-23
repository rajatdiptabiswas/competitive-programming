#!/usr/bin/env python3


INDEX = 0
VALUE = 1


def main():
	n,x = map(int, input().split())
	a_input = [int(x) for x in input().split()]
	a = [[i,a_input[i]] for i in range(len(a_input))]

	for _ in range(x):
		popped = a[:x]
		remaining = a[x:]

		delete = max(popped, key=lambda x:x[VALUE])
		print(delete[INDEX]+1, end=' ')
		popped.remove(delete)

		for i in range(len(popped)):
			if popped[i][VALUE] != 0:
				popped[i][VALUE] -= 1

		a = remaining + popped

	print()


if __name__ == '__main__':
	main()