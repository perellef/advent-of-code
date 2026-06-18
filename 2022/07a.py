
from collections import defaultdict

with open("2022/07.txt","r") as f:
    linje = [e.rstrip("\n") for e in f.readlines()]

filsystem = defaultdict(list)

sti = []

i = 0
for el in linje[1:]:
    if el.startswith("$"):
        kommando = el.split(" ")[1]
        args = el.split(" ")[2:]
        if kommando == "cd":
            if args[0] == "..":
                sti = sti[:-1]

            else:
                sti.append(args[0])
        continue

    st,fil = el.split()

    if st == "dir":
        continue

    filsystem['-'.join(sti)].append((int(st), fil))

s = 0
for mappe in set(filsystem):
    sum_ = sum(sum(st for (st,_) in direkte_under) for k, direkte_under in filsystem.items() if k.startswith(mappe))
    if sum_ <= 100000:
        s += sum_

print(s)
# 1250377 FEIL