a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

delta = (b**2) - (4*a*c)

if(int(a)==0 or delta<0):
    print("Impossivel calcular") 
    
else:
    r1 = ( -b + (delta**(1/2)) ) / (2*a)
    r2 = ( -b - (delta**(1/2)) ) / (2*a)
    print("R1 = %.5f" %r1)
    print("R2 = %.5f" %r2)
