#!/usr/bin/env python3

from math import sqrt, floor, ceil


def is_perfect_square(n):
    val = sqrt(n)
    
    if val - floor(val) == 0:
        return True
    else:
        return False


def next_num(num):
    # val = int(''.join(num))
    # val += 1
    # new_num = list(str(val))
    # if '0' not in new_num:
    #     return new_num
    # else:
    #     return next_num(new_num)

    i = len(num) - 1
    num_copy = num.copy()

    while i >= 0:
        if num_copy[i] == '9':
            num_copy[i] = '1'
            i -= 1
            continue
        
        num_copy[i] = chr(ord(num_copy[i]) + 1)
        break

    return num_copy


def main():
    t = int(input())

    # max_val = 10**6 * 9**2

    # squares = [0,1]
    
    # for _ in range(int(sqrt(max_val))):
    #     squares.append(squares[-1] + 2*(len(squares)-1) + 1)

    for _ in range(t):
        n = int(input())

        # 1, 4, 9, 16, 25, 36, 49, 64, 81
        # coins = [1, 4, 9, 16, 25, 36, 49, 64, 81]

        num = ['1' for _ in range(n)]
        num_end = ['9' for _ in range(n)]
        
        flag = 0

        while num != num_end:
            num_str = ''.join(num)

            val = 0

            for x in num:
                val += int(x)**2
            
            if is_perfect_square(val):
                print(num_str)
                flag = 1
                break

            # print(num_str)

            num = next_num(num)

        if flag == 0:
            print('-1')


if __name__ == '__main__':
    main()