# løst

with open("2023/10.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

import heapq

heap = [(0,(r,k), "S") for r in range(len(matrise)) for k in range(len(matrise[0])) if matrise[r][k] == "S"]

avstander = {}
while heap:
    d, (r,k), må_være = heapq.heappop(heap)

    if r < 0 or r >= len(matrise) or k < 0 or k >= len(matrise[0]):
        continue
    if matrise[r][k] not in må_være:
        continue
    if (r,k) in avstander:
        continue

    avstander[(r,k)] = d

    if matrise[r][k] in "|JLS": # opp
        heapq.heappush(heap, (d+1, (r-1,k), "|F7"))
    if matrise[r][k] in "-LFS": # til høyre
        heapq.heappush(heap, (d+1, (r, k+1), "-7J"))
    if matrise[r][k] in "-7JS": # til venstre
        heapq.heappush(heap, (d+1, (r, k-1), "-LF"))
    if matrise[r][k] in "|F7S": # ned
        heapq.heappush(heap, (d+1, (r+1, k), "|JL"))

print(max(avstander.values()))
# 6682

