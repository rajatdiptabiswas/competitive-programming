from sys import stdin, stdout


def diamond(room):
	room = str(room)

	even = 0
	odd = 0

	for x in range(len(room)):
		val = int(room[x])

		if (val%2 == 0):
			even += val
		else:
			odd += val

	ans = abs(even - odd)

	return ans


def main():
	t = int(stdin.readline())
	# t = int(input())

	prefix_room = [0 for i in range(2*1000001)]
	diamond_answer = [0 for j in range(1000001)]

	for x in range(1, 2000002):
		prefix_room[x] = prefix_room[x-1] + diamond(x)

	for y in range(1, 1000001):
		diamond_answer[y] = diamond_answer[y-1] + (2 * (prefix_room[(2*y)-1] - prefix_room[y])) + diamond(2*y)

	while(t != 0):
		q = int(stdin.readline())
		# q = int(input())

		stdout.write(str(diamond_answer[q]) + "\n")
		# print(diamond_answer[q])

		t -= 1


if __name__ == '__main__':
	main()