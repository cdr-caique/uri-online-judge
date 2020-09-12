n = int(input())
out = ""

for i in range (n):
    hash_value = 0
    l = int(input())
    
    for element in range (l):
        position = 0
        s = str(input())
        
        for ch in s:
            alphabet = int(ord(ch)) - 65
            hash_value += alphabet + element + position
            position += 1
        
    out += str(hash_value) + "\n"
        
out = out[:-1]
print(out)
