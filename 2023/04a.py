# løst 

with open("2023/04.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0
for el in linjer:
    l1,l2 = el.split(": ")[1].split(" | ")

    lst1 = [e for e in l1.split(" ") if e != '']
    lst2 = [e for e in l2.split(" ") if e != '']

    matcher = len(set(lst1).intersection(set(lst2)))

    if matcher == 0:
        continue

    s += 2**(matcher-1)

print(s)
# 33950

