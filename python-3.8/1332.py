n = int(input())
out = ""

for i in range(n):
    s = str(input())

    if(len(s) > 3):
        out += "3\n"
        
    else:
        total = 0
        
        if(s[0] == "o"):
            total += 1
        if(s[1] == "n"):
            total += 1
        if(s[2] == "e"):
            total += 1
        
        if(total >= 2):
            out += "1\n"
        
        else:
            out += "2\n"
        
out = out[:-1]
print(out)
