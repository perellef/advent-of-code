# løst

with open("2024/10.txt","r") as f:
    topografi = [e.rstrip("\n") for e in f.readlines()]

from collections import defaultdict

høyder = defaultdict(set)

for r in range(len(topografi)):
    for k in range(len(topografi[0])):
        høyder["." if topografi[r][k] == "." else int(topografi[r][k])].add((r,k))

stimatrise = defaultdict(int)
for r,k in høyder[9]:
    stimatrise[(r,k)] = 1

retninger = [(0,1),(0,-1),(1,0),(-1,0)]

for h in range(9,0,-1):
    for r,k in høyder[h-1]:
        stimatrise[(r,k)] = sum(stimatrise[(r+dr,k+dk)] for dr,dk in retninger if (r+dr,k+dk) in høyder[h])
        
print(sum(stimatrise[(r,k)] for (r,k) in høyder[0]))
# 1511