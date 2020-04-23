#!/usr/bin/env python3


def main():
    t = int(input())

    for test in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        count = 7
        flag = True
        one_found = False

        for i in range(n):
            if arr[i] == 1:
                one_found = True
                if count < 6:
                    flag = False
                    break
                count = 1
            else:
                if not one_found:
                    continue
                count += 1
        
        if flag:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
