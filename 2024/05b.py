
from collections import defaultdict

with open("2024/05.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

i = linjer.index("")


indekser = {}

ks = set(int(e.split("|")[0]) for e in linjer[:i])
vs = set(int(e.split("|")[1]) for e in linjer[:i])

ns = ks.union(vs)
indekser = []
while True:
    neste = ns.difference(indekser)
    for e in linjer[:i]:
        k,v = e.split("|")
        if int(k) in neste:
            neste.discard(int(v))

    for n in neste:
        indekser.append(n)
    if len(neste) == 0:
        break

etter = defaultdict(set)
for e in linjer[:i]:
    k,v = e.split("|")
    etter[int(k)].add(int(v)) 

def er_gyldig(ns):
    brukt = set()
    for n in ns:
        if len(etter[n].intersection(brukt)) > 0:
            return False
        brukt.add(n)
    return True

s = 0
for e in linjer[i+1:]:
    ns = [int(n) for n in e.split(",")]
    
    if not er_gyldig(ns):
        sorted_ns = list(sorted(ns, key=lambda x: indekser.index(x)))
        s += sorted_ns[len(sorted_ns)//2]

print(s)
# 5391