def main():
    n = int(input())
    c = input().strip()  
    p = input().strip() 
    
    g = [[] for _ in range(6)]
    
    for i in range(n):
        if p[i] == c[i]:
            continue
        
        if p[i] == 'C':
            if c[i] == '-':
                g[0].append(i + 1)  
            else:
                g[4].append(i + 1)  
        elif p[i] == 'M':
            if c[i] == '-':
                g[3].append(i + 1)  
            else:
                g[1].append(i + 1)  
        elif p[i] == '-':
            if c[i] == 'C':
                g[5].append(i + 1)  
            else:
                g[2].append(i + 1)  
    
    ans = []
    
    def put(i, ty):
        assert len(g[i]) > 0
        ans.append((g[i].pop(), ty))
    
    if len(g[1]) > len(g[4]):
        put(0, 1)  
        while len(g[4]): 
            put(1, 3)  
            put(4, 3)  
        put(1, 3)  
        if len(g[2]):
            put(2, 2)  
        ans[-1] = (ans[-1][0], 2)  
        
        while len(g[1]): 
            put(0, 1)  
            put(1, 3)  
            if len(g[2]): 
                put(2, 2) 
            ans[-1] = (ans[-1][0], 2)  
        while len(g[5]): 
            put(0, 1)  
            put(5, 2)  
        while len(g[2]): 
            put(3, 1)  
            put(2, 2)  
    
    elif len(g[1]) < len(g[4]):
        put(3, 1)  
        while len(g[1]): 
            put(4, 3) 
            put(1, 3)  
        put(4, 3) 
        if len(g[5]):
            put(5, 2)  
        ans[-1] = (ans[-1][0], 2)  
        
        while len(g[4]): 
            put(3, 1)  
            put(4, 3)  
            if len(g[5]):
                put(5, 2)  
            ans[-1] = (ans[-1][0], 2)  
        while len(g[2]): 
            put(3, 1)  
            put(2, 2)  
        while len(g[5]): 
            put(0, 1)  
            put(5, 2)  
    
    else:
        if len(g[1]): 
            if len(g[0]): 
                put(0, 1)  
                while len(g[1]): 
                    put(1, 3)  
                    put(4, 3)  
                if len(g[5]):
                    put(5, 2) 
                ans[-1] = (ans[-1][0], 2)  
            else:
                assert len(g[3])  
                put(3, 1)  
                while len(g[4]): 
                    put(4, 3)  
                    put(1, 3)  
                if len(g[2]):
                    put(2, 2) 
                ans[-1] = (ans[-1][0], 2)  
        
        while len(g[2]): 
            put(3, 1)  
            put(2, 2)  
        while len(g[5]): 
            put(0, 1)  
            put(5, 2)  
    
    cmds = []
    for v, c in ans:
        cmds.append(f"DRIVE {v}")
        if c // 2:
            cmds.append("DROPOFF")
        if c % 2:
            cmds.append("PICKUP")
    
    print(len(cmds))
    for cmd in cmds:
        print(cmd)
 
if __name__ == "__main__":
    main()