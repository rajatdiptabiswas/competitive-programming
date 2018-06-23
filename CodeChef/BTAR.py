#!/usr/bin/env python3


def main():
	t = int(input())

	while (t != 0):
		n = int(input())
		a = [0 for i in range(4)] # counts the number of mod 0, 1, 2, 3
		array = [int(x) for x in input().split()] # given array

		for x in range(n):
			a[(array[x] % 4)] += 1 # populates the count array

		if (a[1]*1 + a[2]*2 + a[3]*3) % 4 == 0: # sum of the mod x no of mods is divisible by 4
			ans = min(a[1], a[3]) # creates all 1+3=4 possibilites
			a[1] -= ans # remaining mod 1
			a[3] -= ans # remaining mod 3
			ans += a[2]//2 # adds all 2+2=4 possibilites
			a[2] -= (a[2]//2) * 2 # remaining mod 2

			if (a[2] != 0): # single mod 2 remains
				ans += 2 # 2+1+1 or 2+3+3 possibilities
				
				if (a[1] != 0):
					a[1] -= 2

				if (a[3] != 0):
					a[3] -= 2

			if (a[1]): # mod 1 still remains
				ans += (a[1]//4) * 3 # 1+1+1+1 in 3 steps

			if (a[3]): # mod 3 still remains
				ans += (a[3]//4) * 3 # 3+3+3+3 in 3 steps

			print(ans)

		else: # sum of the mod x no of mods is not divisible by 4
			print("-1")

		t -= 1


if __name__ == '__main__':
	main()