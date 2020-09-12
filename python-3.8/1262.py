out = ""

while True:
    try:
        cicles,aux = 0,0
        s = str(input())
        p = int(input())
        
        for ch in s:
            if(ch == 'W'):
                cicles += 1
                if(0<aux<=p):
                    cicles += 1
                aux = 0
                
            elif(ch == 'R'):
                if(aux == p):
                    cicles += 1
                    aux = 1
                else:
                    aux += 1
        
        if(0<aux<=p):
            cicles += 1
        
        out += str(cicles) + "\n"
    
    except EOFError:
        break
    
out = out[:-1]
print(out)
