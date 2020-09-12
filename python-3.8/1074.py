n = int(input())

message = ""

for i in range(n):
    x = int(input())
    if(x==0):
        message += "NULL\n"
    elif(x%2 == 0):
        message += "EVEN "
        if(x > 0):
            message += "POSITIVE\n"
        else:
            message += "NEGATIVE\n"
    else:
        message += "ODD "
        if(x > 0):
            message += "POSITIVE\n"
        else:
            message += "NEGATIVE\n"
            
message = message[:-1]
print(message)
