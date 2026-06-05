# løst

with open("2023/14.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

def transpose(m):
    return [''.join(m[r][k] for r in range(len(m))) for k in range(len(m[0]))]

m = ['#'.join(''.join(sorted(el, reverse=True)) for el in e.split("#")) for e in transpose(matrise)]

s = 0
for e in m:
   for i,char in enumerate(reversed(e), start=1):
       if char == "O":
           s += i
print(s)
# 109665
