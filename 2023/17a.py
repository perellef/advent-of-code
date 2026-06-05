# løst

import heapq

with open("2023/17.txt","r") as f:
    matrise = [[int(el) for el in e.rstrip("\n")] for e in f.readlines()]

heap = [(0, (0,0), (">",0))]
besøkte = set()

while True:
    (v, (r,k), (retn,n)) = heapq.heappop(heap)

    if (r,k) == (len(matrise)-1, len(matrise[0])-1):
        print(v+matrise[r][k]-matrise[0][0])
        break

    if ((r,k), (retn,n)) in besøkte:
        continue
    if r < 0 or k < 0 or r >= len(matrise) or k >= len(matrise[0]):
        continue

    besøkte.add(((r,k), (retn,n)))

    if retn in "<>":
        heapq.heappush(heap,(v+matrise[r][k], (r-1,k), ("^",1)))
        heapq.heappush(heap, (v+matrise[r][k], (r+1,k), ("v",1)))
    else: # ^v
        heapq.heappush(heap, (v+matrise[r][k], (r,k-1), ("<",1)))
        heapq.heappush(heap, (v+matrise[r][k], (r,k+1), (">",1)))

    if n == 3:
        continue

    if retn == ">":
        heapq.heappush(heap, (v+matrise[r][k], (r,k+1), (retn,n+1)))
    elif retn == "<":
        heapq.heappush(heap, (v+matrise[r][k], (r,k-1), (retn,n+1)))
    elif retn == "v":
        heapq.heappush(heap, (v+matrise[r][k], (r+1,k), (retn,n+1)))
    else:  # retn == "^""
        heapq.heappush(heap, (v+matrise[r][k], (r-1,k), (retn,n+1)))

# 814