# løst

from collections import defaultdict 

with open("2025/04.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

papir = defaultdict(int)
for rad, linje in enumerate(linjer):
    for kol, tegn in enumerate(linje):
        if tegn == "@":
            papir[(rad,kol)] +=1


etter = sum(papir.values())    
aksessbar_papir = set()

while True:
    før = etter
    for rad, linje in enumerate(linjer):
        for kol, tegn in enumerate(linje):

            if tegn != "@" and (kol,tegn) not in aksessbar_papir:
                continue
            antall = (papir[(rad+1,kol)] 
                + papir[(rad+1,kol+1)]
                + papir[(rad+1,kol-1)]
                + papir[(rad-1,kol)]
                + papir[(rad-1,kol+1)]
                + papir[(rad-1,kol-1)]
                + papir[(rad,kol+1)]
                + papir[(rad,kol-1)]
            )

            if antall < 4:
                aksessbar_papir.add((rad,kol))
                papir[(rad,kol)] = 0

    etter = sum(papir.values())
    if før == etter:
        break
    
print(len(aksessbar_papir))
# 8758