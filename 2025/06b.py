# løst

with open("2025/06.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]
linjer = [e for e in linjer if e != ""]

operasjon = {
    "*": (lambda a, b: a*b),
    "+": (lambda a, b: a+b),
}

s = 0
operasjoner_index = {}
for i,tegn in enumerate(linjer[len(linjer)-1]):
    if tegn in ("*","+"):
        operasjoner_index[i] = tegn

for i in range(len(linjer[0])):
    if i in operasjoner_index:
        alle_tall = [] 
        op = linjer[-1][i]

    if i+1 not in operasjoner_index:
        tall = ""
        for t in range(len(linjer)-1):
            tall += linjer[t][i]
        
        alle_tall.append(int(tall.replace(" ", "")))

    if i+1 in operasjoner_index or i == len(linjer[0])-1:
        p = 1 if op=="*" else 0
        for tall in alle_tall:
            p = operasjon[op](p, tall)
        s += p

print(s)
# 9770311947567