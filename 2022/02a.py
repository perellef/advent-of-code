# løst

with open("2022/02.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

poeng1 = {"A": 1, "B": 2, "C": 3}
poeng2 = {"X": 1, "Y": 2, "Z": 3}

s = 0
for h1, h2 in linjer:
    if poeng1[h1] == poeng2[h2]:
        s += poeng2[h2] + 3
    elif (poeng1[h1]-poeng2[h2]) % 3 == 2:
        s += poeng2[h2] + 6
    else:
        s += poeng2[h2]

print(s)
# 9177