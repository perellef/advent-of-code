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

støttes_av = defaultdict(list)
støtter = defaultdict(list)

for x1,y1,z1 in sortert:
    for x2,y2,z2 in sortert:
        if z1[1] == z2[0] - 1 and overlapper_xy(x1,y1,x2,y2):
            støtter[(x1,y1,z1)].append((x2,y2,z2))
            støttes_av[(x2,y2,z2)].append((x1,y1,z1))

s = 0
for kloss in sortert:
    s += int(all((len(støttes_av[e]) > 1 for e in støtter[kloss])))

print(s)
# 459