#!/usr/bin/env python3

from itertools import product
from collections import Counter


def g0(c):
    m = {
        '0':0,
        '1':1,
        'a':0,
        'A':1
    }
    return m[c]


def g1(c):
    m = {
        '0':0,
        '1':1,
        'a':1,
        'A':0
    }
    return m[c]


def operation(op, prod):
    ans = []
    for x,y in prod:
        if op == '|':
            ans.append((g0(x) | g0(y), g1(x) | g1(y)))
        elif op == '&':
            ans.append((g0(x) & g0(y), g1(x) & g1(y)))
        elif op == '^':
            ans.append((g0(x) ^ g0(y), g1(x) ^ g1(y)))
    return ans


def next_operation(op, inputs, g0_g1):
    ans = []
    # for x in inputs:
    #     for g_0,g_1 in g0_g1:
    #         if op == '|':
    #             ans.append((g0(x) | g_0, g1(x) | g_1))
    #         elif op == '&':
    #             ans.append((g0(x) & g_0, g1(x) & g_1))
    #         elif op == '^':
    #             ans.append((g0(x) ^ g_0, g1(x) ^ g_1))
    #         print(x, op, '(', g_0, g_1, ') = ', ans[-1])

    for g_0,g_1 in g0_g1:
        for x in inputs:
            if op == '|':
                ans.append((g0(x) | g_0, g1(x) | g_1))
            elif op == '&':
                ans.append((g0(x) & g_0, g1(x) & g_1))
            elif op == '^':
                ans.append((g0(x) ^ g_0, g1(x) ^ g_1))
            print('(', g_0, g_1, ')', op, x, '=', ans[-1])

    return ans


def countxcount(op, count1, count2):
    ans = []
    for p,q in count1:
        for x,y in count2:
            if op == '|':
                ans.append((p | x, q | y))
            elif op == '&':
                ans.append((p & x, q & y))
            elif op == '^':
                ans.append((p ^ x, q ^ y))
            print('({}, {}) {} ({}, {}) = {}'.format(p, q, op, x, y, ans[-1]))
    return Counter(ans)


def fast_countxcount(op, counter1, counter2):
    ans = {
        (0, 0): 0, 
        (0, 1): 0, 
        (1, 0): 0, 
        (1, 1): 0
    }
    for p,q in counter1:
        for x,y in counter2:
            if op == '|':
                out = (p | x, q | y)
                ans[out] += counter1[(p,q)] * counter2[(x,y)]
            elif op == '&':
                out = (p & x, q & y)
                ans[out] += counter1[(p,q)] * counter2[(x,y)]
            elif op == '^':
                out = (p ^ x, q ^ y)
                ans[out] += counter1[(p,q)] * counter2[(x,y)]
    return ans


def get_count(op):
    items =  [x for x in product(inputs, inputs)]
    # for i in items:
    #     print(i)
    op_list = operation(op, items)
    # for o in op_list:
    #     print(o)
    print(op_list)

    count = Counter(op_list)

    return count


def proportion(counter):
    total = sum(counter.values())
    for val in counter:
        print(val, counter[val]/total)


def pq_inverse(counter):
    total = sum(counter.values())
    q_inverse = pow(total, mod-2, mod)
    
    print(((counter[(0,0)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(1,1)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(0,1)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(1,0)] % mod) * (q_inverse)) % mod, end=' ')

    print()


def xor_count(counter):
    ans = {
        (0,0) : counter[(0,0)] + counter[(0,1)] + counter[(1,0)] + counter[(1,1)],
        (0,1) : counter[(0,0)] + counter[(0,1)] + counter[(1,0)] + counter[(1,1)],
        (1,0) : counter[(0,0)] + counter[(0,1)] + counter[(1,0)] + counter[(1,1)],
        (1,1) : counter[(0,0)] + counter[(0,1)] + counter[(1,0)] + counter[(1,1)]        
    }
    return ans


def and_count(counter):
    ans = {
        (0,0) : 4*counter[(0,0)] + 2*counter[(0,1)] + 2*counter[(1,0)] + 1*counter[(1,1)],
        (0,1) : 0*counter[(0,0)] + 2*counter[(0,1)] + 0*counter[(1,0)] + 1*counter[(1,1)],
        (1,0) : 0*counter[(0,0)] + 0*counter[(0,1)] + 2*counter[(1,0)] + 1*counter[(1,1)],
        (1,1) : 0*counter[(0,0)] + 0*counter[(0,1)] + 0*counter[(1,0)] + 1*counter[(1,1)]        
    }
    return ans


def or_count(counter):
    ans = {
        (0,0) : 1*counter[(0,0)] + 0*counter[(0,1)] + 0*counter[(1,0)] + 0*counter[(1,1)],
        (0,1) : 1*counter[(0,0)] + 2*counter[(0,1)] + 0*counter[(1,0)] + 0*counter[(1,1)],
        (1,0) : 1*counter[(0,0)] + 0*counter[(0,1)] + 2*counter[(1,0)] + 0*counter[(1,1)],
        (1,1) : 1*counter[(0,0)] + 2*counter[(0,1)] + 2*counter[(1,0)] + 4*counter[(1,1)]        
    }
    return ans


inputs = ['0', '1', 'a', 'A']

AND = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 1), (1, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 0), (1, 0), (0, 0), (1, 0)]
OR = [(0, 0), (1, 1), (0, 1), (1, 0), (1, 1), (1, 1), (1, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1), (1, 0), (1, 1), (1, 1), (1, 0)]
XOR = [(0, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 0), (1, 0), (0, 1), (0, 1), (1, 0), (0, 0), (1, 1), (1, 0), (0, 1), (1, 1), (0, 0)]
ALL = [(0, 0), (0, 1), (1, 0), (1, 1)]

mod = 998244353

counter_and = {
    (0, 0): 9, 
    (0, 1): 3, 
    (1, 0): 3, 
    (1, 1): 1
}

counter_or = {
    (1, 1): 9, 
    (0, 1): 3, 
    (1, 0): 3, 
    (0, 0): 1
}

counter_xor = {
    (0, 0): 4, 
    (1, 1): 4, 
    (0, 1): 4, 
    (1, 0): 4
}

counter_base = {
    (0, 0): 1, 
    (1, 1): 1, 
    (0, 1): 1, 
    (1, 0): 1
}


def expression_eval(string):

    curr_counter = counter_base

    if string == '#':
        return curr_counter
  
    stack = list() 
  
    # traversing string from the end
    n = len(string)
    
    for i in range(n-1, -1, -1): 
        
        if (string[i] == "("): 
            
            s = list() 
  
            while (stack[-1] != ")"): 
                s.append(stack[-1]) 
                stack.pop()
            stack.pop() 
  
            # for AND and OR operations
            if (len(s) == 3): 
                if s[1] == "&": 
                    curr_counter = and_count(curr_counter)
                elif s[1] == '|': 
                    curr_counter = or_count(curr_counter)
                elif s[1] == '^':
                    curr_counter = xor_count(curr_counter)
                stack.append('#') 
              
        else: 
            stack.append(string[i]) 
  
    
    return curr_counter


def main():
    # t = int(input())

    # for testcase in range(t):
    #     string = input()
        
    #     counter = expression_eval(string)

    #     pq_inverse(counter)

    print(countxcount('&', XOR, XOR))
    print(fast_countxcount('^', counter_base, counter_base))

    ans = list()


if __name__ == '__main__':
    main()
