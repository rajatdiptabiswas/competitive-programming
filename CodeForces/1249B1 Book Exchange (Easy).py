#!/usr/bin/env python3


def find(array, start, target):
    current = start
    count = 1

    while True:
        if current == target:
            return count
        current = array[current-1]
        count += 1


def main():
    t = int(input())

    for testcase in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        for i in range(n):
            print(find(arr, arr[i], i+1), end=' ')
        print()


if __name__ == '__main__':
    main()