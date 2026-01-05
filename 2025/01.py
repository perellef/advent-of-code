with open("01.txt","r") as f:
    linjer = [e for e in f.readlines()]

# === 1a ====

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


# === 1b ====

antall_0_passeringer = 0
s = 50
for linje in linjer:
    forrige = s
    if linje.startswith("R"):
        s = (s + int(linje[1:]))
    else:
        s = (s - int(linje[1:]))
    
    if s >= 100:
        antall_0_passeringer += s//100
    elif s <= 0:
        antall_0_passeringer += abs(s-100)//100
        if forrige == 0:
            antall_0_passeringer -= 1

    s = s%100

print(antall_0_passeringer)
# 6671