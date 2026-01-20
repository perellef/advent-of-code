# løst

from collections import defaultdict

with open("2025/07.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

startlaser = [[(i,l) for l in range(len(linjer[i])) if linjer[i][l]=='S'] for i in range(len(linjer))]
startlaser = [e for elem in startlaser for e in elem][0]

splittere = [[(i,l) for l in range(len(linjer[i])) if linjer[i][l]=='^'] for i in range(len(linjer))]
splittere = list(sorted([e for elem in splittere for e in elem]))
splittere = [e for e in splittere if e[0] > startlaser[0]]

lasere = defaultdict(int)
lasere[startlaser[1]] += 1

s = 0
for i,(_,x) in enumerate(splittere):
    if x in lasere:
        s += 1

        lasere[x+1] += lasere[x]
        lasere[x-1] += lasere[x]
        lasere.pop(x)

print(sum(lasere.values()))
# 12895232295789