# Minimum Distances HackerRank
# https://www.hackerrank.com/challenges/minimum-distances/problem

n = int(input())

arr = []
arr = [int(n) for n in input().split()]

small = arr[0]
flag = 0

for y in range(0,n):
	for z in range(y+1,n):
		# print("small = ", small)
		# print("y = %d; z = %d" % (y, z))

		if arr[y] == arr[z]:
			# print("y = %d; z = %d" % (y, z))
			if abs(y-z) <= small:
				# print("abs y-z = ", abs(y-z))
				# print("arr[y] = ", arr[y], "; arr[z] = ", arr[z])
				small = abs(y-z)
				flag = 1

if flag == 1:
	print(small)
else:
	print("-1")
