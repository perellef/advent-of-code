# løst

with open("2023/11.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

rads = [r for r in range(len(matrise)) if set(matrise[r]) == set(('.',))]
kols = [k for k in range(len(matrise[0])) if set([matrise[r][k] for r in range(len(matrise))]) == set(('.',))]

galakser = [(r,k) for r in range(len(matrise)) for k in range(len(matrise[0])) if matrise[r][k] == "#"]
galaksepar = [(g1,g2) for g1 in galakser for g2 in galakser if (g1 > g2)]

s = 0
for (r1,k1), (r2,k2) in galaksepar:
    ekstra_r = len([r for r in rads if min(r1,r2) < r and r < max(r1,r2)])
    ekstra_k = len([k for k in kols if min(k1,k2) < k and k < max(k1,k2)])

    s += abs(k1-k2) + abs(r1-r2) + ekstra_r+ekstra_k
print(s)

# 9734203