def is_good(n):
    if (n-2)%4 == 0:
        return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    prod = []
    val = 0
    count = 0

    for i in range(len(arr)):
        val = arr[i]
        if is_good(val):
            count += 1
        for j in range(i+1, len(arr)):
            val *= arr[j]
            if is_good(val):
                count += 1

    print(count)
