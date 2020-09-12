out = ""

while True:
    try:
        equation = str(input())
        equation = equation.replace('=','+')
        equation = equation.split('+')
        
        if equation[0].isdigit() == False:
            out += str ( int(equation[2]) - int(equation[1]) ) + "\n"
            
        elif equation[1].isdigit() == False:
            out += str ( int(equation[2]) - int(equation[0]) ) + "\n"
            
        elif equation[2].isdigit() == False:
            out += str ( int(equation[0]) + int(equation[1]) ) + "\n"

    except EOFError:
        break
    
out = out[:-1]
print(out)
