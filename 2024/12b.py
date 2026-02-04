# løst

with open("2024/12.txt","r") as f:
    område = [e.rstrip("\n").split(" ")[0] for e in f.readlines()]

besøkte = set()
hager = []

def er_hage(bokstav, r,k):
    return r >= 0 and k >= 0 and r < len(område) and k < len(område[0]) and område[r][k] == bokstav

def breddesøk(bokstav, r,k):
    if not er_hage(bokstav, r,k):
        return
    if (r, k) in besøkte:
        return
    besøkte.add((r,k))
        
    hager[-1][1] += 1
    
    # ytterhjørner
    if not er_hage(bokstav, r+1,k) and not er_hage(bokstav, r,k-1):
        hager[-1][0] += 1
    if not er_hage(bokstav, r,k-1) and not er_hage(bokstav, r-1,k):
        hager[-1][0] += 1
    if not er_hage(bokstav, r-1,k) and not er_hage(bokstav, r,k+1):
        hager[-1][0] += 1
    if not er_hage(bokstav, r,k+1) and not er_hage(bokstav, r+1,k):
        hager[-1][0] += 1

    # innerhjørner
    if er_hage(bokstav, r+1,k) and er_hage(bokstav, r,k-1) and not er_hage(bokstav, r+1,k-1):
        hager[-1][0] += 1
    if er_hage(bokstav, r,k-1) and er_hage(bokstav, r-1,k) and not er_hage(bokstav, r-1,k-1):
        hager[-1][0] += 1
    if er_hage(bokstav, r-1,k) and er_hage(bokstav, r,k+1) and not er_hage(bokstav, r-1,k+1):
        hager[-1][0] += 1
    if er_hage(bokstav, r,k+1) and er_hage(bokstav, r+1,k) and not er_hage(bokstav, r+1,k+1):
        hager[-1][0] += 1

    breddesøk(bokstav, r+1, k)
    breddesøk(bokstav, r-1, k)
    breddesøk(bokstav, r, k+1)
    breddesøk(bokstav, r, k-1)

for r in range(len(område)):
    for k in range(len(område[0])):
        if (r,k) in besøkte:
            continue
            
        hager.append([0,0])
        breddesøk(område[r][k],r,k)

print(sum(kanter*areal for kanter,areal in hager))
# 893676