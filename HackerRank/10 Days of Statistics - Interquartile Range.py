#!/usr/bin/env python3


def median(array):
    n = len(array)

    if n % 2 == 0:
        return (array[n//2-1] + array[n//2])/2
    else:
        return array[n//2]


def main():
    num = int(input())
    elements = [int(x) for x in input().split()]
    freq = [int(y) for y in input().split()]

    array = []

    for i in range(num):
        for x in range(freq[i]):
            array.append(elements[i])

    array = sorted(array)
    n = len(array)

    if not n % 2 == 0:
        left = array[:n//2]
        right = array[n//2+1:]
    else:
        left = array[:n//2]
        right = array[n//2:]

    ans = median(right) - median(left)

    print(float(ans))


if __name__ == '__main__':
    main()