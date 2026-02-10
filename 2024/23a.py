# løst

with open("2024/23.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

from collections import defaultdict

koblinger = defaultdict(set)

for el in inp:
    a,b = el.split("-")
    koblinger[a].add(b)
    koblinger[b].add(a)

grupper_3 = set()

for n1,v in koblinger.items():
    for n2 in v:
        for n3 in koblinger[n2]:
            if n3 in v:
                gruppe = tuple(sorted((n1,n2,n3)))
                grupper_3.add(gruppe)

grupper_3 = [e for e in grupper_3 if any(el.startswith("t") for el in e)]

print(len(grupper_3))
# 1200