# løst

with open("2023/09.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0
for linje in linjer:
    tall = [int(e) for e in linje.split(" ")]
    alle_tall = [tall]
    while True:
        nye_tall = [alle_tall[-1][t+1]-alle_tall[-1][t] for t in range(len(alle_tall[-1])-1)]

        alle_tall.append(nye_tall)
        if nye_tall.count(0) == len(nye_tall):
            break

    f = 0
    for t in range(len(alle_tall)-2,-1,-1):
        f = alle_tall[t][0] - f
    s += f
print(s)
# 1016