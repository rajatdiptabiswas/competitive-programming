#!/usr/bin/env python3


def main():
    t = int(input())

    for testcase in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        d = [int(y) for y in input().split()]

        ans = -1

        for i in range(n):
            if (a[(i-1)%n] + a[(i+1)%n]) < d[i]:
                if ans < d[i]:
                    ans = d[i]

        print(ans)


if __name__ == '__main__':
    main()