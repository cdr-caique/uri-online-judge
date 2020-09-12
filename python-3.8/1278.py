out = ""
aux = 0

while True:
    n = int(input())

    if n == 0:
        break
    
    if aux == 1:
        out += "\n"
    
    l = []
    
    for i in range(n):
        s = input().split()
        s = " ".join(s)
        l.append(s)
        
    m = max(len(i) for i in l)

    for i in range(len(l)):
        for j in range(m-len(l[i])):
            out += " "
        out += l[i] + "\n"

    aux = 1

out = out[:-1]
print(out)
