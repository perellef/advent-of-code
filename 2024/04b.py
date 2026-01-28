# løst

with open("2024/04.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

s = 0
for k in range(1,len(matrise)-1):
    for r in range(1,len(matrise[0])-1):
        
        if matrise[k][r] == "A":
            ms1 = matrise[k+1][r-1]+matrise[k-1][r+1]
            ms2 = matrise[k+1][r+1]+matrise[k-1][r-1]
        
            if ms1 in ("MS","SM") and ms2 in ("MS","SM"):
                s += 1
        
print(s)
# 2003