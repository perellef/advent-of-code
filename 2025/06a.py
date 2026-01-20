# løst

with open("2025/06.txt","r") as f:
    linjer = [e.rstrip("\n").split() for e in f.readlines()]

linjer = [e for e in linjer if e != "" ]

operasjon = {
    "*": (lambda a, b: a*b),
    "+": (lambda a, b: a+b),
}

s = 0
for i in range(len(linjer[0])):
    op = linjer[-1][i]
    p = 1 if op=="*" else 0
    for t in range(len(linjer)-1):
        p = operasjon[op](p, int(linjer[t][i]))
    s += p
print(s)
# 6891729672676
