#!/usr/bin/env python3


def is_list_empty(l):
    return all(map(is_list_empty, l)) if isinstance(l, list) else False


def main():
    t = int(input())

    for testcase in range(t):
        rows = int(input())
        
        table = []

        for _ in range(rows):
            arr = [int(x) for x in input().split()]
            table.append(arr[1:])

        # print(table)

    chef_total = 0

    while not is_list_empty(table):
        chef_index = -1
        opp_index = -1

        chef_max = 0
        opp_max = 0

        for i in range(len(table)):
            if len(table[i]) == 0:
                continue
            
            if chef_max < table[i][0]:
                chef_max = table[i][0]
                chef_index = i

            if opp_max < table[0][-1] and len(table[i]) != 1:
                opp_max = table[i][-1]
                opp_index = i

        if chef_index != opp_index:
            chef_total += chef_max
            table[chef_index].pop(0)
            table[opp_index].pop(-1)

    print(chef_max)


if __name__ == '__main__':
    main()