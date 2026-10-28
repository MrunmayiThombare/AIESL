import heapq

def manhattan(init,goal):
    distance=0
    for i in range(9):
        val = init[i]
        if val != 0:
            j = goal.index(val)
            ir = i // 3
            ic = i % 3
            gr = j // 3
            gc= j % 3
            distance = abs(ir-gr) + abs(ic-gc)
    return distance

def getMoves(curr):
    moves=[]
    empty=curr.index(0)
    dir=[-3,3,-1,1]
    for i in dir:
        new = empty + i
        if 0 <= new <= 8:
            if empty % 3 == 0 and i == -1:
                continue
            if empty % 3 == 2 and i == 1:
                continue
            newList = list(curr)
            newList[empty] = newList[new]
            newList[new]=0
            moves.append(tuple(newList))
    return moves

def astar(init, goal):
    q = [(manhattan(init, goal), 0, init, [init])]
    best = {init: 0}
    while q:
        f, g, s, p = heapq.heappop(q)
        if s == goal: return p
        for n in getMoves(s):
            c = g + 1
            if c < best.get(n, float('inf')):
                best[n] = c; heapq.heappush(q, (c + manhattan(n, goal), c, n, p + [n]))
    return None

goal = (1,2,3,8,0,4,7,6,5)
print("Enter initial state in a list : ")
init = tuple(map(int, input().split()))
solution = astar(init,goal)
if solution != None:
    for s in solution:
        print('------')
        print(f"{s[0]} {s[1]} {s[2]}")
        print(f"{s[3]} {s[4]} {s[5]}")
        print(f"{s[6]} {s[7]} {s[8]}")
else:
    print("No solution exists !!")