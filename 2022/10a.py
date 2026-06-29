# løst

with open("2022/10.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

X = 1

indre_sykel = 0
i = 0

s = 0

sykler = 1
while i < len(linjer):
    sykler += 1

    l = linjer[i]
    if l[:4] == "noop":
        i += 1
    elif l[:4] == "addx":
        if indre_sykel == 0:
            indre_sykel += 1
        else:
            indre_sykel = 0
            X += int(l.split(" ")[-1])
            i += 1

    if sykler % 40 == 20:
        s += sykler*X

print(s)
# 11960