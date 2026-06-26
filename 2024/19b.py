# løst

from collections import defaultdict
import heapq

with open("2024/19.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

design = set(linjer[0].split(", "))
patterns = linjer[2:]

m = max([len(d) for d in design])

def designkombinasjoner(pattern):
    totale = defaultdict(int)
    totale[""] = 1
    
    neste = [(0, "")]
    besøkt = set()

    while neste:
        _,p = heapq.heappop(neste)

        for i in range(min(m, len(pattern)-len(p))):
            n = pattern[len(p):len(p)+i+1]
            if n in design:
                totale[p+n] += totale[p]
                if p+n in besøkt:
                    continue

                besøkt.add(p+n)
                heapq.heappush(neste, (len(p+n),p+n))
    
    return totale[pattern]

s = 0
for p in patterns:
    s += designkombinasjoner(p)
print(s)
# 571894474468161