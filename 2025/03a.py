# løst

with open("2025/03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0 
for linje in linjer:
    sifre = [int(e) for e in linje]
    max_ = max(sifre)
    ind = sifre.index(max_)
    if ind == len(sifre)-1:
        smax_ = max(sifre[:-1])
        t = int(str(smax_) + str(max_))
    else:
        smax_ = max(sifre[ind+1:])
        t = int(str(max_) + str(smax_))
    s += t
print(s)
#17087
