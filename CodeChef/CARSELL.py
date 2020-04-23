#!/usr/bin/env/python3


mod = 1000000007


def main():
    t = int(input())

    for tc in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        total = 0

        arr.sort(reverse=True)

        for i in range(n):
            add = max(arr[i] - i, 0)
            total += add % mod
            total %= mod

        print(total)

        
if __name__ == '__main__':
    main()
