v = input().split()

a, b, c = float(v[0]), float(v[1]), float(v[2])
pi = 3.14159

a_tri = a*c/2
a_cir = pi*(c**2)
a_tra = (a+b)*c/2
a_qua = b**2
a_ret = a*b

print("TRIANGULO: %.3f" %a_tri)
print("CIRCULO: %.3f" %a_cir)
print("TRAPEZIO: %.3f" %a_tra)
print("QUADRADO: %.3f" %a_qua)
print("RETANGULO: %.3f" %a_ret)
