def win(b, p):
    return any(all(b[i] == p for i in line) for line in
    [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
     (1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def mini(b, comp):
    if win(b, 'O'): return 1
    if win(b, 'X'): return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if comp else 'X'
            scores.append(mini(b, not comp))
            b[i] = ' '
    return (max if comp else min)(scores)

b = [' '] * 9
while True:
    print(b[:3], b[3:6], b[6:])
    i = int(input("X position (0-8): "))
    if i not in range(9) or b[i] != ' ':
        print("Invalid")
        continue
    b[i] = 'X'
    if win(b, 'X'): print("Human wins"); break
    if ' ' not in b: print("Draw"); break
    moves = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            moves.append((mini(b, False), i))
            b[i] = ' '
    _, i = max(moves)
    b[i] = 'O'
    if win(b, 'O'): print("Computer wins"); break
    if ' ' not in b: print("Draw"); break
