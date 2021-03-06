#!/usr/bin/env python3


def is_good(n):
    if (n-2) % 4 == 0:
        return False
    else:
        return True


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
       
        val = 0
        count = 0
        
        for i in range(len(arr)):
            val = arr[i] % 100
            if is_good(val):
                count += 1
            for j in range(i+1, len(arr)):
                val *= arr[j]
                val %= 100
                if is_good(val):
                    count += 1

        print(count)


if __name__ == '__main__':
    main()
