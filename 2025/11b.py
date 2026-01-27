# løst
 
from collections import defaultdict

with open("2025/11.txt","r") as f:
    treehash = {e.split(": ")[0]: e.rstrip("\n").split(" ",1)[1].split(" ") for e in f.readlines()}

forfedre = defaultdict(list)
for n,v in treehash.items():
    for k in v:
        forfedre[k].append(n)    

def treesøk(fra,til,unåelig):
    if fra == til:
        return 1
    if fra in unåelig:
        return 0
    return sum(treesøk(v,til,unåelig) for v in treehash[fra]) 

p = 1
for fra, til in (("svr","fft"), ("fft","dac"), ("dac","out")): 
    unåelig = set(("out",))
    unåelig.discard(til)
    while True:
        len_for = len(unåelig)
        for k in unåelig.copy():
            for v in forfedre[k]:
                if v == til:
                    continue
                if all((vv in unåelig) for vv in treehash[v]):
                    unåelig.add(v)

        len_etter = len(unåelig)
        if len_for == len_etter:
            break

    p *= treesøk(fra,til,unåelig)

print(p)
# 306594217920240