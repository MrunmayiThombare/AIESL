from itertools import product
nodes = ['a','b','c','d']
colors = ['red','blue','green']
neighbours = [('a','b'),('a','c'),('b','c'),('c','d'),('b','d')]

for p in product(colors,repeat=len(nodes)):
    valid = True
    d = dict(zip(nodes,p))
    for x,y in neighbours:
        if d[x] == d[y]:
            valid = False
            break

    if valid : 
        print(d)
