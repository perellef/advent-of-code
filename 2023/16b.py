# løst

with open("2023/16.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

m = 0

starter = ([((i, 0),">") for i in range(len(matrise))]
    + [((i, len(matrise[0])-1),"<") for i in range(len(matrise))]
    + [((0, i),"v") for i in range(len(matrise[0]))]
    + [((len(matrise)-1, i),"^") for i in range(len(matrise[0]))])

for s in starter:
    lst = [s]

    besøkte = set()
    while lst:
        ((r,k),retn) = lst.pop()

        if ((r,k),retn) in besøkte:
            continue
        if r < 0 or k < 0 or r >= len(matrise) or k >= len(matrise[0]):
            continue
        besøkte.add(((r,k),retn))

        if retn+matrise[r][k] in (">.", ">-", "^-", "v-", "^/", "v\\"):
            lst.append(((r,k+1),">"))
        if retn+matrise[r][k] in ("<.", "<-", "^-", "v-", "v/", "^\\"):
            lst.append(((r,k-1), "<"))
        if retn+matrise[r][k] in ("^.", "^|", "<|", ">|", ">/", "<\\"):
            lst.append(((r-1,k), "^"))
        if retn+matrise[r][k] in ("v.", "v|", "<|", ">|", "</", ">\\"):
            lst.append(((r+1,k), "v"))

    m = max(m, len(set(e[0] for e in besøkte)))

print(m)    
# 8231