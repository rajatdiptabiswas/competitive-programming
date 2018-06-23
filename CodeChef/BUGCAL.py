#!/usr/bin/env python3


def main():
	t = int(input())

	while t != 0:
		a, b = map(int, input().split())

		exp = 0
		final_ans = 0

		while max(a, b) > 0:
			a_digit = a % 10
			b_digit = b % 10

			ans = a_digit + b_digit

			if ans > 9:
				ans -= 10

			ans *= 10 ** exp
			exp += 1

			final_ans += ans

			a //= 10
			b //= 10

		print(final_ans)

		t -= 1


if __name__ == '__main__':
	main()