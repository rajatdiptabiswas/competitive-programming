#!/usr/bin/env python3

def charge(x):
	x += 1
	return x

def discharge(x):
	x -= 2
	return x

a,b = map(int, input().split())

# print("a = " + str(a) + " b = " + str(b))

ans = 0

while(a > 0 and b > 0):
	if a == 1 and b == 1:
		break

	elif a >= b:
		a = discharge(a)
		b = charge(b)

	else:
		a = charge(a)
		b = discharge(b)

	# print("a = " + str(a) + " b = " + str(b))
	
	ans += 1

print(ans)