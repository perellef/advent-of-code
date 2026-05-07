# løst 

with open("2023/04.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

skrapelodd = {int(e.removeprefix("Card ").split(": ")[0]): 1 for e in linjer}

s = 0
for kortnr,el in enumerate(linjer, start=1):
    l1,l2 = el.split(": ")[1].split(" | ")

    lst1 = [e for e in l1.split(" ") if e != '']
    lst2 = [e for e in l2.split(" ") if e != '']

    matcher = len(set(lst1).intersection(set(lst2)))

    for i in range(1, matcher+1):
        skrapelodd[kortnr+i] += skrapelodd[kortnr]

print(sum(skrapelodd.values()))
# 14814534