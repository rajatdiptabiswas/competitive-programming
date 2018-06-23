#!/usr/bin/env python3

t = int(input())

while t != 0:
	n = int(input())
	a = [int(x) for x in input().split()]
	inv_count = 0
	local_inv_count = 0

	if (n == 1):
		print("YES")
		t -= 1
		continue

	else:
		for i in range(1,n):
			if a[i-1] > a[i]:
				inv_count += 1

			for j in range(i,n):
				if a[i-1] > a[j]:
					local_inv_count += 1

		if (inv_count == local_inv_count):
			print("YES")

		else:
			print("NO")

	t -= 1