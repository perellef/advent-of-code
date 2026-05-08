# løst

with open("2023/10.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

matrise = ["."+e+"." for e in matrise]
matrise = ['.'*len(matrise[0])]+matrise+['.'*len(matrise[0])]


r,k = [(r,k) for r in range(len(matrise)) for k in range(len(matrise[0])) if matrise[r][k] == "S"][0]

opp = matrise[r-1][k] in "|F7"
ned = matrise[r+1][k] in "|JL"
th = matrise[r][k+1] in "-7J"
tv = matrise[r][k-1] in "-LF"

if opp and ned: starttegn = "|"
if opp and th: starttegn = "L"
if opp and tv: starttegn = "J"
if ned and tv: starttegn = "7"
if ned and th: starttegn = "F"
if th and tv: starttegn = "-"

if opp: neste = (r-1,k)
elif ned: neste = (r+1,k)
elif tv: neste = (r,k-1)

hjørner = []
if starttegn in "F7JL":
    hjørner.append((r,k))

besøkt = set()
besøkt.add((r,k))
while True:
    r,k = neste

    if matrise[r][k] in "F7JL":
        hjørner.append((r,k))
    besøkt.add((r,k))

    if matrise[r][k] in "|JL" and (r-1,k) not in besøkt: # opp
        neste = (r-1,k)
    elif matrise[r][k] in "|F7" and (r+1,k) not in besøkt: # ned
        neste = (r+1,k)
    elif matrise[r][k] in "-LF" and (r,k+1) not in besøkt: # th
        neste = (r,k+1)
    elif matrise[r][k] in "-7J" and (r,k-1) not in besøkt: # tv
        neste = (r,k-1)
    else:
        break

s = 0
for i in range(len(hjørner)):
    h1 = hjørner[(i-1)%len(hjørner)]
    h2 = hjørner[i]
    
    s += h1[0]*h2[1] - h1[1]*h2[0]

areal = abs(s)/2
areal -= len(besøkt)/2-1

print(int(areal))
# 353