#!/usr/bin/env python3


def main():
	n,q = map(int, input().split())
	a = [int(x) for x in input().split()]

	for i in range(q):
		ques = [int(a) for a in input().split()]

		if ques[0] == 1:
			a[ques[1] - 1] = ques[2]

		elif ques[0] == 2:
			l = ques[1]
			r = ques[2]
			sub = a[l-1:r]
			sub.sort(reverse=True)

			x = 0
			while True:
				if x+2 >= len(sub):
					print(0)
					break
				if sub[x+1] + sub[x+2] > sub[x]:
					print(sub[x] + sub[x+1] + sub[x+2])
					break
				else:
					x += 1
					continue


if __name__ == '__main__':
	main()