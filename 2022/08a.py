# løst

with open("2022/08.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

rader = [[(r,k) for k in range(len(matrise[0]))] for r in range(len(matrise))]
rader_rev = [[(r,k) for k in range(len(matrise[0])-1,-1,-1)] for r in range(len(matrise))]
kolonner = [[(r,k) for r in range(len(matrise))] for k in range(len(matrise[0]))]
kolonner_rev = [[(r,k) for r in range(len(matrise)-1,-1,-1)] for k in range(len(matrise[0]))]

kan_ses = set()
for fra_kant in (rader, rader_rev, kolonner, kolonner_rev):
    for rad in fra_kant:
        største = -1
        for r,k in rad:
            if int(matrise[r][k]) > største:
                største = int(matrise[r][k])
                kan_ses.add((r,k))

print(len(kan_ses))
# 1832

