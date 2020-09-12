p1 = input().split()
p2 = input().split()

c1, n1, v1 = int(p1[0]), int(p1[1]), float(p1[2])
c2, n2, v2 = int(p2[0]), int(p2[1]), float(p2[2])

v1 = n1*v1
v2 = n2*v2
vt = v1+v2

print("VALOR A PAGAR: R$ %.2f" %vt)
