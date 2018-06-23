 #!/usr/bin/env python3


def main():
    t = int(input())

    for testcase in range(t):
        x,N = map(int, input().split())
        
        full_sum=((N*(N+1)//2)-x)
        
        if (full_sum % 2) != 0:
            print("impossible")
            continue
        
        if N == 2 or N == 3:
            print("impossible")
            continue
        
        required_sum=(full_sum)//2
        
        sum = required_sum
        
        p_set = set()
        e = N
        
        while e >= 1:
            if x == e:
                e = e-1
                continue
                
            sum = sum - e
            p_set.add(e)
                    
            if sum == 0:
                break
                
            if sum < 0 or sum == x:
                p_set.remove(e)
                sum = sum+e
            
            e = e-1
        
        if sum != 0:
            print("impossible")
        
        if sum == 0:
            e = 1
            
            while e <= N:
                if e in p_set:
                    print("1",end='')
                elif e == x:
                    print("2",end='')
                else:
                    print("0",end='')
                e = e+1
            
            print("")


if __name__ == '__main__':
    main()