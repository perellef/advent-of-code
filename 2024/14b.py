# løst

with open("2024/14.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

from collections import defaultdict

B = 101
H = 103

n = 0
while True:
    nhash = defaultdict(int)
    for e in inp:
        start_x = int(e.split(",")[0].split("=")[1])
        start_y = int(e.split(",")[1].split(" ")[0])
        
        ax = int(e.split("v=")[1].split(",")[0])
        ay = int(e.split("v=")[1].split(",")[1])

        x = (start_x+n*ax)%B
        y = (start_y+n*ay)%H

        nhash[(x,y)] += 1

    if all((v==1) for v in nhash.values()):
        break
    n += 1
    
print(n)
# 6532