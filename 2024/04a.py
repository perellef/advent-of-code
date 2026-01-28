# løst

with open("2024/04.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

horisontale = matrise
verikale = [''.join([e[i] for e in matrise]) for i in range(len(matrise))]
th_diagonal = [''.join([matrise[r][r-d] for r in range(len(matrise)) if 0 <= r-d < len(matrise[0])]) for d in range(-(len(matrise) - 1), len(matrise[0]))]
tv_diagonal = [''.join([matrise[len(matrise)-r-1][r-d] for r in range(len(matrise)) if 0 <= r-d < len(matrise[0])]) for d in range(-(len(matrise) - 1), len(matrise[0]))]

linjer = (horisontale + verikale + th_diagonal + tv_diagonal)

s = 0
for linje in linjer:
    for i in range(len(linje)-3):
        s += int(linje[i:i+4] in ("XMAS", "SAMX"))
print(s)
# 2549

