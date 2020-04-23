#!/usr/bin/env python3


mod = 998244353

counter_base = {
    (0, 0): 1,  
    (0, 1): 1, 
    (1, 0): 1,
    (1, 1): 1
}


def pq_inverse(counter):
    total = sum(counter.values())
    q_inverse = pow(total, mod-2, mod)
    
    print(((counter[(0,0)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(1,1)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(0,1)] % mod) * (q_inverse)) % mod, end=' ')
    print(((counter[(1,0)] % mod) * (q_inverse)) % mod, end=' ')

    print()


def counter_x_counter(op, counter1, counter2):
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


def expression_eval(expr):
    curr_counter = counter_base

    if expr == '#':
        return curr_counter
  
    stack = list() 
  
    n = len(expr)    
    for i in range(n-1, -1, -1):
        # print(stack)
        if (expr[i] == "("): 
            s = list() 
            while (stack[-1] != ")"):
                s.append(stack[-1]) 
                stack.pop()
            stack.pop() 
            if (len(s) == 3): 
                ans = counter_x_counter(s[1], s[0], s[2])
            stack.append(ans)
        elif (expr[i] == '#'):
            stack.append(counter_base)   
        else: 
            stack.append(expr[i]) 
    
    return stack[-1]



def main():
    t = int(input())

    for testcase in range(t):
        string = input()
        
        counter = expression_eval(string)

        pq_inverse(counter)


if __name__ == '__main__':
    main()
