#!/usr/bin/env python3


def two_gen(l,r):
    if min(l,r) == 0:
        return max(l,r)+1

    upper_limit = min(l,r)+1
    digits = l+r+1

    total = 0
    for i in range(1, digits//2+1):
        total += 2 * min(i, upper_limit)

    if digits % 2 == 1:
        total += upper_limit

    return total


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x)%4 for x in input().split()]
        two_count = 0

        for i in range(n):
            left_odds = 0
            right_odds = 0
            if arr[i] == 2:
                k = i-1
                while k >= 0 and arr[k] % 2 == 1:
                    left_odds += 1
                    k -= 1
                k = i+1
                while k < n and arr[k] % 2 == 1:
                    right_odds += 1
                    k += 1
                two_count += two_gen(left_odds, right_odds)

        count = ((n)*(n+1))//2
        count -= two_count

        print(count)


if __name__ == '__main__':
    main()
