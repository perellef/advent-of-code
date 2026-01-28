# løst

with open("2024/01.txt","r") as f:
    linjer = [e.rstrip("\n").split("   ") for e in f.readlines()]

lst1 = [int(e[0]) for e in linjer]
lst2 = [int(e[1]) for e in linjer]

from collections import defaultdict

ns = defaultdict(int)
for n in lst2:
    ns[n] += 1

s = 0
for n in lst1:
    s += n*ns[n]
print(s)
# 24931009