# løst

with open("2024/01.txt","r") as f:
    linjer = [e.rstrip("\n").split("   ") for e in f.readlines()]

lst1 = [int(e[0]) for e in linjer]
lst2 = [int(e[1]) for e in linjer]

s = 0
for a,b in zip(sorted(lst1),sorted(lst2)):
    s += abs(a-b)
print(s)
# 2066446