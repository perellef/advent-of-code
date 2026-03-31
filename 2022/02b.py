# løst

with open("2022/02.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

poeng1 = {"A": 1, "B": 2, "C": 3}

s = 0
for h1, h2 in linjer:
    if h2 == "Y":
        s += poeng1[h1] + 3
    elif h2 == "X":
        s += (poeng1[h1]-2) % 3 + 1
    else:
        s += (poeng1[h1]) % 3 + 1 + 6

print(s)
# 12111