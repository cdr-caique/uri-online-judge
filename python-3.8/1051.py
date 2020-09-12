v = float(input())

if(0 <= v <= 2000):
    print("Isento")
if(2000 < v <= 3000):
    v8 = (v-2000)*8/100
    imposto = v8
    print("R$ %.2f" %imposto)
if(3000 < v <= 4500):
    v8 = (1000)*8/100
    v18 = (v-3000)*18/100
    imposto = v8 + v18
    print("R$ %.2f" %imposto)
if(4500 < v):
    v8 = (1000)*8/100
    v18 = (1500)*18/100
    v28 = (v-4500)*28/100
    imposto = v8 + v18 + v28
    print("R$ %.2f" %imposto)
