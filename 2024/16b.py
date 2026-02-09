# løst

import heapq

with open("2024/16.txt","r") as f:
    kart = [e.rstrip("\n") for e in f.readlines()]


start = [(k,r) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "S"][0]
slutt = [(k,r) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "E"][0]


retninger = {
    "sør": [(0,1), ("vest", "øst")],
    "vest": [(-1,0), ("nord", "sør")],
    "nord": [(0,-1), ("øst", "vest")],
    "øst": [(1,0), ("sør", "nord")]
}

besøkte = {}
lst = [(0, start, "øst", set())]

stitiles = set((slutt,))
optimal = 100000000

while len(lst) > 0:
    score, pos, retning, tiles = heapq.heappop(lst)
    x,y = pos

    if score > optimal:
        break

    if x < 0 or x >= len(kart[0]) or y < 0 or y >= len(kart):
        continue
    if kart[y][x] == "#":
        continue
    
    if (pos, retning) in besøkte and besøkte[(pos, retning)][0] < score:
        continue
    besøkte[(pos, retning)] = (score, tiles)

    if pos == slutt:
        optimal = score
        stitiles = stitiles.union(tiles)
        continue

    dx,dy = retninger[retning][0]

    heapq.heappush(lst, (score+1, (x+dx,y+dy), retning, tiles.union(((x,y),))))
    for ny_retning in retninger[retning][1]:
        heapq.heappush(lst, (score+1000, (x,y), ny_retning, tiles.copy()))

print(len(stitiles))
# 529, 188.278s