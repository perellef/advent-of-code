# løst

from collections import defaultdict

with open("2024/06.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

startpos = [(r,k) for r in range(len(matrise)) for k in range(len(matrise[0])) if matrise[r][k] == "^"][0]
startretning = (-1,0)

rotasjon = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0)
}

def besøker(start, retning, matrise):
    # returnerer tom-mengde = loop

    pos = start
    besøkt = defaultdict(set)
    while True:
        r,k = pos
        if retning in besøkt[pos]:
            return set()
        besøkt[pos].add(retning)

        if any((
            r == 0,
            k == 0,
            r == len(matrise)-1,
            k == len(matrise[0])-1
        )):
            break

        r_ny = r+retning[0]
        k_ny = k+retning[1]

        if matrise[r_ny][k_ny] == "#":
            retning = rotasjon[retning]
        else:
            pos = (r_ny, k_ny)
    return set(besøkt)

sti = besøker(startpos, startretning, matrise)

s = 0
for r,k in sti:
    blokkert_matrise = [list(e) for e in matrise]
    blokkert_matrise[r][k] = "#"

    if (r,k) == startpos:
        continue
    
    bes = besøker(startpos, startretning, blokkert_matrise)
    if len(bes) == 0:
        s += 1

print(s)
# 1951, 41.064s