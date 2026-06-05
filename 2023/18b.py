# løst

with open("2023/18.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

koords = [(0,0)]

sn = 0
for _,_,hex in linjer:
    r = hex[-2]
    n = int(hex[2:-2], 16)

    if r == "0":
        koords.append((koords[-1][0], koords[-1][1]+n))
    elif r == "1":
        koords.append((koords[-1][0]+n, koords[-1][1]))
    elif r == "2":
        koords.append((koords[-1][0], koords[-1][1]-n))
    elif r == "3":
        koords.append((koords[-1][0]-n, koords[-1][1]))
    sn += int(n)

s = 0
for i in range(len(koords)-1):
    x1,y1 = koords[i]
    x2,y2 = koords[i+1]

    s += x1*y2 - x2*y1

print(int(abs(s)/2+sn/2+1))
# 78242031808225