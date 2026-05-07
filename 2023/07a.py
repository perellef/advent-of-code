# løst
 
with open("2023/07.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

VALØRER = "23456789TJQKA" 

from collections import defaultdict

def korttype(kort):
    like = defaultdict(int) 
    for k in kort:
        like[k] += 1
    styrke = tuple((v,VALØRER.index(k)) for k,v in like.items())
    antall = tuple(sorted(styrke, reverse=True))

    if antall[0][0] == 1:
        return 0
    if antall[0][0] == 2:
        return antall[1][0]
    if antall[0][0] == 3:
        return 3+antall[1][0]
    if antall[0][0] == 4:
        return 6
    if antall[0][0] == 5:
        return 7
    raise ValueError


korthender = []
for el in linjer:
    kort, bid = el.split(" ")
    korthender.append(((korttype(kort), tuple((VALØRER.index(k) for k in kort))), int(bid)))

s = 0
for rank,(_,bid) in enumerate(sorted(korthender, reverse=False),start=1):
    s += rank*bid

print(s)
# 247815719