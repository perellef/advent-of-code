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

            i = -1
            while True:
                i += 1
                ant_r, ant_k = r1+i*dr,k1+i*dk
                if min(ant_r,ant_k) < 0 or ant_r >= len(matrise) or ant_k >= len(matrise[0]):
                    break
                antinoder.add((ant_r,ant_k))

            
            i = -1
            while True:
                i += 1
                ant_r, ant_k = r2-i*dr,k2-i*dk
                if min(ant_r,ant_k) < 0 or ant_r >= len(matrise) or ant_k >= len(matrise[0]):
                    break
                antinoder.add((ant_r, ant_k))

print(len(antinoder))
# 839