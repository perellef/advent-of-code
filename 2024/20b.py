# løst

with open("2024/20.txt","r") as f:
    kart = [e.rstrip("\n") for e in f.readlines()]

start = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "S"][0]
slutt = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "E"][0]

def avstander_fra(pos):
    avstander = {}

    i = 0
    neste = [pos]
    while True:
        nye_neste = []
        for n in neste:
            if min(n) < 0 or n[0] >= len(kart) or n[1] >= len(kart[0]):
                continue
            if kart[n[0]][n[1]] == "#":
                continue
            if n in avstander:
                continue
            avstander[n] = i

            nye_neste.append((n[0]+1, n[1]))
            nye_neste.append((n[0]-1, n[1]))
            nye_neste.append((n[0], n[1]+1))
            nye_neste.append((n[0], n[1]-1))
        
        neste = nye_neste
        if len(neste) == 0:
            break
        i += 1
    return avstander

avstander_fra_start = avstander_fra(start)
avstander_fra_slutt = avstander_fra(slutt)

vanlig = avstander_fra_slutt[start]

s = 0
for pos1,tid1 in avstander_fra_start.items():
    for pos2,tid2 in avstander_fra_slutt.items():
        gap = abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

        s += int(gap <= 20 and vanlig-(tid1+tid2+gap) >= 100)
        
print(s)
# 985482  114.40s