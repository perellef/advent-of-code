# løst

from collections import defaultdict 

with open("2025/05.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

spl = linjer.index("")

ranges_str = [(int(e.split("-")[0]),int(e.split("-")[1])) for e in linjer[:spl]]
available = linjer[spl+1:]

alle = []
def avail(x):
    for a,b in ranges_str:
        if a <= x and x <= b:
            alle.append(x)
            return
        
for x in available:
    avail(int(x))
    
print(len(alle))
# 848