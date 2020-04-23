#!/usr/bin/env python3

import math


def main():
    t = int(input())

    for tc in range(t):
        n = int(input())

        ans = []

        if n <= 3:
            ans.append([i for i in range(1,n+1)])
        else:
            ans.append([1,2,3])
            for i in range(4, n-1, 2):
                ans.append([i, i+1])
            if n % 2 == 0:
                ans.append([n])
            else:
                ans.append([n-1, n])

        # print(ans)

        print(len(ans))
        
        for item in ans:
            print(len(item), *item)


if __name__ == '__main__':
    main()
