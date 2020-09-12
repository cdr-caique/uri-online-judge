n = int(input())

leds = 0
out = ""

for i in range(n):
    
    v = str(input())
    leds = 0
    
    for c in v:
        if(c=="1"):
            leds += 2
            continue
        elif(c=="2"):
            leds += 5
            continue
        elif(c=="3"):
            leds += 5
            continue
        elif(c=="4"):
            leds += 4
            continue
        elif(c=="5"):
            leds += 5
            continue
        elif(c=="6"):
            leds += 6
            continue
        elif(c=="7"):
            leds += 3
            continue
        elif(c=="8"):
            leds += 7
            continue
        elif(c=="9"):
            leds += 6
            continue
        elif(c=="0"):
            leds += 6
    
    out += str(leds) + " leds\n"
    
out = out[:-1]
print(out)
