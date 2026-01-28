# løst

from collections import defaultdict

with open("2024/05.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

i = linjer.index("")

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
    if er_gyldig(ns):
        s += ns[len(ns)//2]

print(s)
# 5391