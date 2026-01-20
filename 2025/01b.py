# løst

with open("2025/01.txt","r") as f:
    linjer = [e for e in f.readlines()]

antall_0 = 0
s = 50
for linje in linjer:
    if linje.startswith("R"):
        s = (s + int(linje[1:]))%100
    else:
        s = (s - int(linje[1:]))%100

    if s == 0:
        antall_0 += 1

print(antall_0)
# 1152
