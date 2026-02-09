# løst

with open("2024/22.txt","r") as f:
    inp = [int(e.rstrip("\n")) for e in f.readlines()]

def neste(secret):
    a = secret * 64
    secret ^= a
    secret %= 16777216

    b = secret // 32
    secret ^= b
    secret %= 16777216

    c = secret * 2048
    secret ^= c
    secret %= 16777216

    return secret

from collections import defaultdict

tot = defaultdict(int)

l = 0
aper = []
for f in inp:
    l += 1
    if l % 100 == 0:
        print("-",l)
    aper.append(set())

    fire_siste = []
    for i in range(2000):
        n = neste(f)
        fire_siste.append((n%10)-(f%10))
        
        f = n

        if len(fire_siste)<4:
            continue

        if tuple(fire_siste) not in aper[-1]:
            aper[-1].add(tuple(fire_siste))
            tot[tuple(fire_siste)] += n%10
        fire_siste.pop(0)

print(max(tot.values()))
# 2277