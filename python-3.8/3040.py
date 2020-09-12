n = int(input())
out = ""

for i in range(n):
    h, d, g = input().split()
    h, d, g = int(h), int(d), int(g)
        
    out += "Sim\n" if(200<=h<=300 and d>=50 and g>=150) else "Nao\n"
    
out = out[:-1]
print(out)
