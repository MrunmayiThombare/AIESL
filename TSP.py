from itertools import permutations

dist = []

n = int(input("Enter number of locations for tsp : "))
print("Enter distance matrix row-by-row : ")

for i in range(n):
    row=list(map(int, input().split()))
    dist.append(row)

best_path=[]
best_cost=float("inf")

for p in permutations(range(1,n)):
    path = [0] + list(p) + [0]
    cost=0

    for i in range(n):
       cost += dist[path[i]][path[i+1]]

    if cost < best_cost:
        best_cost=cost
        best_path=path

print("Optimal path : ",best_path)
print("Cost : ",best_cost)