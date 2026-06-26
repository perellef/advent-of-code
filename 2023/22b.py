# løst

from collections import defaultdict

with open("2023/22.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

klosser = [tuple((min(int(e1),int(e2)), (max(int(e1),int(e2)))) for e1,e2 in zip(el.split("~")[0].split(","), el.split("~")[1].split(","))) for el in linjer]
sortert = list(sorted(klosser, key=lambda x: x[2][1]))

def overlapper_xy(x1,y1,x2,y2):
    return x1[0] <= x2[1] and x2[0] <= x1[1] and y1[0] <= y2[1] and y2[0] <= y1[1]

def fall_ned(i, kloss, sortert):
    x1,y1,z1 = kloss
    for x2,y2,z2 in reversed(sortert[:i]):
        if overlapper_xy(x1,y1,x2,y2):
            sortert[i] = x1,y1,(z2[1]+1,z2[1]+1+z1[1]-z1[0])
            return
    sortert[i] = x1,y1,(0,z1[1]-z1[0])

for i, kloss in enumerate(sortert):
    fall_ned(i, kloss, sortert)
    sortert = list(sorted(sortert[:i+1], key=lambda x: x[2][1]))+sortert[i+1:]

støttes_av = defaultdict(set)
støtter = defaultdict(set)

for x1,y1,z1 in sortert:
    for x2,y2,z2 in sortert:
        if z1[1] == z2[0] - 1 and overlapper_xy(x1,y1,x2,y2):
            støtter[(x1,y1,z1)].add((x2,y2,z2))
            støttes_av[(x2,y2,z2)].add((x1,y1,z1))


kjedereaksjon = defaultdict(set)

def ødelegg(falne, forrige):
    nye_forrige = set()
    for f in forrige:
        for v in støtter[f]:
            if len(støttes_av[v].difference(falne)) > 0:
                continue
            nye_forrige.add(v)
            falne.add(v)
    if len(nye_forrige) == 0:
        return len(falne)-1
    return ødelegg(set(falne), nye_forrige)

print(sum(ødelegg(set((e,)), set((e,))) for e in sortert))
# 75784