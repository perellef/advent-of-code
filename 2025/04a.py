# løst

from collections import defaultdict 

with open("2025/04.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

papir = defaultdict(int)
for rad, linje in enumerate(linjer):
    for kol, tegn in enumerate(linje):
        if tegn == "@":
            papir[(rad,kol)] +=1


aksessbar_papir = set()
for rad, linje in enumerate(linjer):
    for kol, tegn in enumerate(linje):

        if tegn != "@": 
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
        
print(len(aksessbar_papir))
# 1397
