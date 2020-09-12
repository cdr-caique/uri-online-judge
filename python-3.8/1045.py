v = input().split(" ")

for i in range(len(v)):
    v[i] = float(v[i])

v = sorted(v)

a, b, c = v[2], v[1], v[0]

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
    
else:
    if(a**2 == (b**2)+(c**2)):
        print("TRIANGULO RETANGULO")
    if(a**2 > (b**2)+(c**2)):
        print("TRIANGULO OBTUSANGULO")
    if(a**2 < (b**2)+(c**2)):
        print("TRIANGULO ACUTANGULO")
    if(a==b==c):
        print("TRIANGULO EQUILATERO")
    elif(a==b or a==c or b==c):
        print("TRIANGULO ISOSCELES")
