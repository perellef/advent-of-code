# løst

with open("2024/07.txt","r") as f:
    tall = [e.rstrip("\n") for e in f.readlines()]

gange = lambda a,b: a*b
pluss = lambda a,b: a+b

operasjoner = [gange, pluss]

s = 0
for t in tall:
    str_p, str_nums = t.split(": ")
    
    ns = [int(e) for e in str_nums.split(" ")]
    p = int(str_p)

    kombs = set((ns[0],))
    for i in range(1,len(ns)):
        kombs = set(operasjon(t,ns[i]) for t in kombs for operasjon in operasjoner)
    if p in kombs:
        s += p

print(s)
# 1620690235709