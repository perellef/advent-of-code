# løst

with open("2022/03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0
for linje in linjer:
    l1 = set(linje[:len(linje)//2])
    l2 = set(linje[len(linje)//2:])
    assert len(l1) == len(l2)

    intersection = list(l1.intersection(l2))
    assert len(intersection) == 1

    v = intersection[0]

    if v == v.capitalize():
        s += ord(v)-38
    else:
        s += ord(v)-96
print(s)
