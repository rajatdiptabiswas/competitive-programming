#!/usr/bin/env python3


def is_good(n):
    if n % 4 == 2:
        return False
    else:
        return True


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        dp = [[None for i in range(n)] for i in range(n)]
        zero_count = 0
        two_count = 0

        for i in range(n):
            zero_count = 0
            for j in range(n-i):
                # fills out first row
                if i == 0:
                    dp[i][j] = arr[j] % 4
                # fills the rest of the rows
                else:
                    dp[i][j] = (dp[i-1][j] * dp[0][i+j]) % 4 
                if not is_good(dp[i][j]):
                    two_count += 1
                if dp[i][j] == 0:
                    zero_count += 1
            if zero_count == n-i:
                break

        count = ((n)*(n+1))//2 - two_count

        for a in dp:
            for i in a:
                if i == None:
                    print('.', end=' ')
                else:
                    print(i, end=' ')
            print()

        print(count)


if __name__ == '__main__':
    main()
