# løst

with open("2022/04.txt","r") as f:
    linjer = [e.rstrip("\n").split(",") for e in f.readlines()]

s = 0
for alv1, alv2 in linjer:
    a1_fra = int(alv1.split("-")[0])
    a1_til = int(alv1.split("-")[1])
    a2_fra = int(alv2.split("-")[0])
    a2_til = int(alv2.split("-")[1])

    if any((
        a1_fra >= a2_fra and a1_til <= a2_til,
        a2_fra >= a1_fra and a2_til <= a1_til,
    )):
        s += 1

print(s)