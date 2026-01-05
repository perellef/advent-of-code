with open("06.txt","r") as f:
    linjer = [e.rstrip("\n").split() for e in f.readlines()]

linjer = [e for e in linjer if e != "" ]

# ==== 6a ====

operasjon = {
    "*": (lambda a, b: a*b),
    "+": (lambda a, b: a+b),
}

s = 0
for i in range(len(linjer[0])):
    op = linjer[-1][i]
    p = 1 if op=="*" else 0
    for t in range(len(linjer)-1):
        p = operasjon[op](p, int(linjer[t][i]))
    s += p
print(s)

# 6891729672676

# ==== 6b ====

with open("06.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

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

"""

s = 0
linjer = [[linjer[t][i] for t in range(len(linjer))] for i in range(len(linjer[0]))]
for linje in linjer:
    op = linje[-1]
    p = 1 if op=="*" else 0

    tall = [] 
    max_tlengde = max(len(linje[i]) for i in range(len(linje)-1))
    for i in range(max_tlengde):
        t = ""
        for l in range(len(linje)-1):
            if len(linje[l]) > i:
                t += linje[l][::-1][i]
        tall.append(t)

    print(tall)
    for t in tall:
        p = operasjon[op](p, int(t))
    
    s += p
print(s)
"""