a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

v1, v2, v3 = False, False, False

if(abs(b-c)<a and a<abs(b+c)):
    v1 = True
if(abs(a-c)<b and b<abs(a+c)):
    v2 = True
if(abs(a-b)<c and c<abs(a+b)):
    v3 = True
    
if(v1==True and v2==True and v3==True):
    per_tri = a+b+c
    print("Perimetro = %.1f" %per_tri)
else:
    area_tra = (a+b)*c/2
    print("Area = %.1f" %area_tra)
