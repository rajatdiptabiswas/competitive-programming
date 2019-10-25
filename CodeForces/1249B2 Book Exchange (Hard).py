#!/usr/bin/env python3


def main():
    t = int(input())

    for testcase in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ans = [0 for _ in range(n)]

        for i in range(n):
            index = i+1
            # no need to perform dfs for elements whose answers are known
            # saves time and computations
            if ans[i] != 0:
                continue
            # if no cycle forms, count = 1
            if arr[i] == index:
                ans[i] = 1
            else:
                current = arr[i]
                count = 1
                # rather than using dfs for each element
                # store the path taken and update with count
                # cycle array stores indices of the path taken for dfs
                cycle = [i]  
                while current != index:
                    current = arr[current-1]
                    count += 1
                    cycle.append(current-1)
                for item in cycle:
                    # store final count in each position stored in cycle array
                    ans[item] = count
        
        for val in ans:
            print(val, end=' ')
        print()


if __name__ == '__main__':
    main()