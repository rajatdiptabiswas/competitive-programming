#!/usr/bin/env python3

num = int(input())

arr = []
arr = [int(n) for n in input().split()]


def isSorted(a):
    # print("len(a) = " + str(len(a))) # debug

    for x in range(0, len(a)-1):
        # print("x = {}".format(x)) # debug
        # print("a[x] = {}; a[x+1] = {}".format(a[x], a[x+1])) # debug
        if a[x] <= a[x+1]:
            check = True
            continue
        else:
            check = False
            break

    # print("check = " + str(check))
    return check


if num == 1 or isSorted(arr) == True:
    print("yes")
    print("1 1")

elif isSorted(arr) == False:
    i = 0

    while i != len(arr):
        if arr[i] < arr[i + 1]:
            i += 1
            continue

        else:
            l = i+1
            break

    # print("l = %d" % (l)) # debug

    i = num-1
    
    while i != -1:
        if arr[i] > arr[i - 1]:
            i -= 1
            continue

        else:
            r = i+1
            break

    # print("r = %d" % (r)) # debug

    i = l-1
    j = r-1

    # print("i = {}; j = {}".format(i, j)) # debug
    
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        i += 1
        j -= 1

    # print(arr) # debug
    # print("isSorted(arr) = " + str(isSorted(arr))) # debug

    if isSorted(arr) == True:
        print("yes")
        print("{} {}".format(l, r))

    else:
        print("no")
