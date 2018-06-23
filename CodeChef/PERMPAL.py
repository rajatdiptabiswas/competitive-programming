#!/usr/bin/env python3

from collections import Counter, deque


def find_indices_of(char, in_string):
	return [index + 1 for index, c in enumerate(in_string) if char == c]


def main():
	t = int(input())

	for test in range(t):
		string = str(input())
		freq = Counter(string)
		# print(freq)
		unique = list(set(string))
		indices = dict()

		for char in unique:
			index = find_indices_of(char, string)
			indices[str(char)] = index

		# print(indices)

		length = len(string)

		odd = 0
		even = 0
		
		for values in freq.values():
			if values % 2 != 0:
				odd += 1
			else:
				even += 1

		if length % 2 == 0 and odd > 0:
			print('-1')
			continue
		elif length % 2 != 0 and odd != 1:
			print('-1')
			continue
		else:
			sides = []
			center = deque()
			for letter, occurrences in freq.items():
				repetitions, odd_count = divmod(occurrences, 2)
				if not odd_count:
					sides.append(letter * repetitions)
					continue
				center.append(letter * occurrences)
			center.extendleft(sides)
			center.extend(sides)

			palindrome = ''.join(center)

			for char in palindrome:
				i = indices[char][0]
				print(str(i), end = ' ')
				indices[char].remove(i)
			print()

			continue


if __name__ == '__main__':
	main()
