# løst

with open("2024/08.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

from collections import defaultdict

antenner = defaultdict(list)

for r in range(len(matrise)):
    for k in range(len(matrise[0])):
        if matrise[r][k] != ".":
            antenner[matrise[r][k]].append((r,k))

antinoder = set()

for frekvens in antenner:
    for (r1,k1) in antenner[frekvens]:
        for (r2,k2) in antenner[frekvens]:
            if (r1,k1) == (r2,k2):
                continue
            dr = r1-r2
            dk = k1-k2

            antinoder.add((r1+dr,k1+dk))
            antinoder.add((r2-dr,k2-dk))

antinoder = [(r,k) for r,k in antinoder if min(r,k) >= 0 and r < len(matrise) and k < len(matrise[0])]

print(len(antinoder))
# 252