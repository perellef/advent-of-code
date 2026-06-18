# løst

with open("2022/08.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

rader = [[(r,k) for k in range(len(matrise[0]))] for r in range(len(matrise))]
rader_rev = [[(r,k) for k in range(len(matrise[0])-1,-1,-1)] for r in range(len(matrise))]
kolonner = [[(r,k) for r in range(len(matrise))] for k in range(len(matrise[0]))]
kolonner_rev = [[(r,k) for r in range(len(matrise)-1,-1,-1)] for k in range(len(matrise[0]))]

distanse = {}
for fra_kant in (rader, rader_rev, kolonner, kolonner_rev):
    for rad in fra_kant:
        største = -1
        for i in range(len(rad)):            
            r,k = rad[i]
            if (r,k) not in distanse:
                distanse[(r,k)] = 1

            if i == len(rad) - 1:
                distanse[(r,k)] *= 0
                continue

            for i2 in range(i+1,len(rad)):
                r2,k2 = rad[i2]

                if matrise[r][k] <= matrise[r2][k2]:
                    break

            distanse[(r,k)] *= i2-i

print(max(distanse.values()))
# 157320