with open("03.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

s = 0 
for linje in linjer:
    sifre = [int(e) for e in linje]
    max_ = max(sifre)
    ind = sifre.index(max_)
    if ind == len(sifre)-1:
        print(1)
        smax_ = max(sifre[:-1])
        t = int(str(smax_) + str(max_))
    else:
        smax_ = max(sifre[ind+1:])
        t = int(str(max_) + str(smax_))
    s += t
print(s)
#17087

# ==== 1b ====

def finn(sifre, n):
    if n == 0:
        return ""
    max_ = max(sifre)
    index = sifre.index(max_)
    
    n_fra_enden = len(sifre)-index
    if n > n_fra_enden:
        return finn(sifre[:index],n-n_fra_enden)+''.join([str(e) for e in sifre[index:]])
    return str(max_)+finn(sifre[index+1:], n-1)


s = 0 
for linje in linjer:
    sifre = [int(e) for e in linje]
    
    t = finn(sifre, 12)
    s += int(t)
print(s)

#169019504359949