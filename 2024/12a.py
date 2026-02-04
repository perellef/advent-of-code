# løst

with open("2024/12.txt","r") as f:
    område = [e.rstrip("\n").split(" ")[0] for e in f.readlines()]

besøkte = set()
hager = []

def breddesøk(bokstav, r,k):
    if r < 0 or k < 0 or r == len(område) or k == len(område[0]):
        hager[-1][0] += 1
        return

    if område[r][k] != bokstav:
        hager[-1][0] += 1
        return

    if (r, k) in besøkte:
        return
        
    hager[-1][1] += 1

    besøkte.add((r,k))
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
# 1494342