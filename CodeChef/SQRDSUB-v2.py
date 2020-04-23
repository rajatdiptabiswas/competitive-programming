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
        arr = [int(x)%4 for x in input().split()]

        val = 0
        two_count = 0
        zero_count = 0

        # for z in arr:
        #     print(z, end=" ")
        # print()

        for i in range(n):
            zero_count = 0
            val = arr[i] % 4
            if not is_good(val):
                two_count += 1
            # print(str(i) + " 0")
            # print(two_count)
            for j in range(i+1,n):
                val *= arr[j] % 4
                val %= 4
                if not is_good(val):
                    two_count += 1
                # print(i,j)
                # print(two_count)
            if zero_count == n-i:
                break

        count = ((n)*(n+1))//2
        
        count -= two_count

        print(count)


if __name__ == '__main__':
    main()
