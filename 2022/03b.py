# løst

with open("2022/03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0
for i in range(0, len(linjer), 3):
    l1 = linjer[i]
    l2 = linjer[i + 1]
    l3 = linjer[i + 2]

    intersection = list(set(l1).intersection(set(l2)).intersection(set(l3)))
    assert len(intersection) == 1

    v = intersection[0]

    if v == v.capitalize():
        s += ord(v)-38
    else:
        s += ord(v)-96
print(s)
# 2508
