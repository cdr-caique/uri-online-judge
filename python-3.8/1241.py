n = int(input())

res = ""

for i in range(n):
    
    a, b = input().split()
    a, b = str(a), str(b)
    
    if(len(a) >= len(b)):
        a = a[(len(a)-len(b)):]
        res += "encaixa\n" if a==b else "nao encaixa\n"
        
    else:
        res += "nao encaixa\n"

res = res[:-1]
print(res)
