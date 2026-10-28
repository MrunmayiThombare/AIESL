from itertools import permutations
a = input("String 1 : ").upper()
b = input("String 2 : ").upper()
c = input("String 3 : ").upper()
letters = set(a+b+c)

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d[a[0]] == 0 or d[b[0]] == 0 or d[c[0]] == 0:
        continue

    x = int(''.join(str(d[i]) for i in a))
    y = int(''.join(str(d[i]) for i in b))
    z = int(''.join(str(d[i]) for i in c))

    if x + y == z:
        print(d)
        print(x, "+", y, "=", z)
        break                                                                                                                                                                                                                                       