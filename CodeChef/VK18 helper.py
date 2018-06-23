a,b = map(int, input().split(' '))

c = 0

for i in range(a,b+1):
	i = str(i)

	# print("-----------------------------------")
	# print("i = {}".format(i))

	even = 0
	odd = 0

	for x in range(len(i)):
		# print("int({}[{}]) = {}".format(i,x,int(i[x])))
		# print("x = {}".format(x))

		val = int(i[x])
		# print("val = {}".format(val))

		if (val%2 == 0):
			even += val
		else:
			odd += val

	ans = abs(even - odd)

	c += ans

	# print("even = {}; odd = {}; even-odd = {}".format(even,odd,even-odd))

	print("{} -> {} -> {}".format(i,ans,c))	