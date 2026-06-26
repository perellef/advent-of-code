# løst

with open("2024/19.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

design = set(linjer[0].split(", "))
patterns = linjer[2:]

m = max([len(d) for d in design])

def er_mulig(pattern):

    neste = set((pattern,))
    while True:
        nye_neste = set()
        for p in neste:
            if p == "":
                return True
            for i in range(m):
                if p[:i+1] in design:
                    nye_neste.add(p[i+1:])
        neste = nye_neste
        if len(neste) == 0:
            return False

s = 0
for p in patterns:
    s += er_mulig(p)
print(s)
# 287
