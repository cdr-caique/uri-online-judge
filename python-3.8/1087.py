moves = ""

while True:
    
    coords = input().split()
    x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])

    if (x1+y1+x2+y2 == 0):
        break
    
    if (x1==x2 and y1==y2):
        moves += "0\n"
        continue
    
    if (x1==x2 or y1==y2):
        moves += "1\n"
        continue
    
    if (abs(x1-x2) == abs(y1-y2)):
        moves += "1\n"
        continue
    
    moves += "2\n"
    
moves = moves[:-1]
print(moves)
