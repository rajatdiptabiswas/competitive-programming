#!/usr/bin/env python3

mod = 1000000007


def main():
    t = int(input())

    for testcase in range(t):
        n = int(input())

        if n == 0:
            print(1)

        elif n == 1:
            print(2)

        else:
            ans = 2 + (3 * n * (n-1))//2 + (n-1)
            ans = int(ans % mod)

            print(ans)

if __name__ == '__main__':
    main()