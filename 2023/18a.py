# løst

with open("2023/18.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

koords = [(0,0)]

sn = 0
for r,n,*_ in linjer:
    if r == "U":
        koords.append((koords[-1][0]-int(n), koords[-1][1]))
    elif r == "L":
        koords.append((koords[-1][0], koords[-1][1]-int(n)))
    elif r == "R":
        koords.append((koords[-1][0], koords[-1][1]+int(n)))
    elif r == "D":
        koords.append((koords[-1][0]+int(n), koords[-1][1]))
    sn += int(n)

s = 0
for i in range(len(koords)-1):
    x1,y1 = koords[i]
    x2,y2 = koords[i+1]

    s += x1*y2 - x2*y1

print(int(abs(s)/2+sn/2+1))
# 39194