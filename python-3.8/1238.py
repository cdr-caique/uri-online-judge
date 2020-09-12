n = int(input())

res = ""

for i in range(n):
    
    s1, s2 = input().split()
    s1, s2 = str(s1), str(s2)
    
    m = min(len(s1), len(s2))
    M = max(len(s1), len(s2))
    
    for x in range(m):
        res += s1[x] + s2[x]
        
    if(m != M):
        for x in range (m, M):
            res += s1[x] if len(s1) > len(s2) else s2[x]

    res += "\n"

res = res[:-1]
print(res)
