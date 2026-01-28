
with open("2024/03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

def er_nummer(s):
    if s[0] == "0":
        return False
    
    return all((t in "0123456789" for t in s))

s = 0
for linje in linjer:
    for do in linje.split("do()"):
        muls = do.split("don't()")[0].split("mul(")
        
        for mul in muls[1:]:
            komma = mul.split(",")

            if len(komma) == 1:
                continue

            parentes = komma[1].split(")")

            m = komma[0]
            n = parentes[0]

            if er_nummer(m) and er_nummer(n):
                s += int(m)*int(n)
print(s)
# 