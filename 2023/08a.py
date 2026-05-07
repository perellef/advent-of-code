# løst

with open("2023/08.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

sekvens = linjer[0]

from collections import defaultdict

keys = {}
for linje in linjer[2:]:
    fra = linje.split(" = ")[0]
    v,h = linje.removesuffix(")").split("(")[1].split(", ")

    keys[fra] = {"L": v, "R": h}

s = 0
nå = "AAA"
while True:
    nå = keys[nå][sekvens[s % len(sekvens)]]
    if nå == "ZZZ":
        break
    s += 1
print(s+1)
# 17141