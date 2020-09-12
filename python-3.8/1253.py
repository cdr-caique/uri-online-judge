n = int(input())

res = ""

for i in range(n):
    
    text = str(input())
    encrypt = int(input())
    text_encripted = ""
    
    for t in text:
        
        pos = ord(t) - encrypt
        text_encripted += chr(91-(65-pos)) if(pos < 65) else chr(ord(t) - encrypt)
    
    res += text_encripted +"\n"  
    
res = res[:-1]
print(res)      
