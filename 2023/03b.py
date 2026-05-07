# løst

with open("2023/03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

linjer = ['.'*len(linjer[0])] + linjer + ['.'*len(linjer[0])]
linjer = ['.'+e+'.' for e in linjer]

sifre = '0123456789'

from collections import defaultdict

gears = defaultdict(list)
for r in range(len(linjer)):

    k = 0
    i = 0
    while k < len(linjer[0]):
        for i in range(len(linjer)-k):
            tegn = linjer[r][k+i]
            if tegn in sifre:
                continue
            if i == 0:
                break
            tall = int(linjer[r][k:k+i])

            for r_ in range(r-1, r+2):
                for k_ in range(k-1, k+i+1):
                    if linjer[r_][k_] == "*":
                        gears[(r_,k_)].append(tall)
            break

        k += i+1

s = 0
for v in gears.values():
    if len(v) == 2:
        s += v[0]*v[1]

print(s)
# 80253814
