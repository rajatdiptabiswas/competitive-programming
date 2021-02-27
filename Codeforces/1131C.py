#!/usr/bin/env python3


def main():
    n = int(input())
    arr = sorted([int(x) for x in input().split()])
    ans = [0 for _ in range(n)]
    rev_arr = arr[::-1]

    x = 0
    y = n-1

    for i in range(0, n, 2):
        ans[x] = arr[i]
        x += 1

    for j in range(1, n, 2):
        ans[y] = arr[j]
        y -= 1

    for val in ans:
        print(val, end=' ')

    print()


if __name__ == '__main__':
    main()