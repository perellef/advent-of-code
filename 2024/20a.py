# løst

with open("2024/20.txt","r") as f:
    kart = [e.rstrip("\n") for e in f.readlines()]

start = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "S"][0]
slutt = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "E"][0]

blokkader = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "#"]

def finn_korteste_veg(blokkader):
    besøkt = set()

    i = 0
    neste = [start]
    while True:
        nye_neste = []
        for n in neste:
            if min(n) < 0 or n[0] >= len(kart) or n[1] >= len(kart[0]):
                continue
            if n in besøkt:
                continue
            besøkt.add(n)
            if n in blokkader:
                continue
            if n == slutt:
                return i

            nye_neste.append((n[0]+1, n[1]))
            nye_neste.append((n[0]-1, n[1]))
            nye_neste.append((n[0], n[1]+1))
            nye_neste.append((n[0], n[1]-1))
        
        neste = nye_neste
        i += 1

vanlig = finn_korteste_veg(set(blokkader))

s = 0
for i in range(len(blokkader)):
    s += int(vanlig-finn_korteste_veg(set(blokkader[:i]+blokkader[i+1:])) >= 100)
print(s)
# 1346  610.684s