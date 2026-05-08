# løst

with open("2023/09.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0
for linje in linjer:
    tall = [int(e) for e in linje.split(" ")]
    while True:
        s += tall[-1]
        nye_tall = [tall[t+1]-tall[t] for t in range(len(tall)-1)]

        if nye_tall.count(0) == len(nye_tall):
            break

        tall = nye_tall
print(s)
# 2098530125