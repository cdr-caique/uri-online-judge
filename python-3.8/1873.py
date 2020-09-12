n = int(input())

game = ['tesoura','pedra','spock','papel','lagarto']
out = ""

for i in range(n):
    s1, s2 = input().split()

    while(game[2] != s1):
        game = [game[-1]] + game[:-1]

    s1 = 2-game.index(s2)
    
    if(s1 > 0):
        out += "rajesh\n"
        
    elif(s1 < 0):
        out += "sheldon\n"
        
    else:
        out += "empate\n"
        
out = out[:-1]
print(out)
