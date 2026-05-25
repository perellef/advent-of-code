# løst

import math

with open("2023/12.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

def løsning_kun_spørsmålstegn(s, tall):
    if len(tall) == 0:
        return 1
    if sum(tall)+len(tall)-1 > len(s):
        return 0
    
    n = len(s)-sum(tall)+1
    r = len(tall)
    return math.comb(n, r)

def antall_løsninger(s, tall):
    sikre = [i for i in range(len(s)) if s[i] == "#"]
    
    if len(tall) == 0:
        return len(sikre) == 0
    if len(sikre) == 0:
        return løsning_kun_spørsmålstegn(s, tall)
    
    sum_ = 0
    for i in range(len(tall)):
        for t in range(max(0, sikre[0]-tall[i]+1), min(sikre[0]+1, len(s)-tall[i]+1)):
            if sum(tall[i+1:])+len(tall[i+1:])-1 > len(s[t+tall[i]+1:]):
                continue
            if len(s) > t+tall[i] and s[t+tall[i]] == "#":
                continue

            l = løsning_kun_spørsmålstegn(s[:max(0, t-1)], tall[:i])
            if l > 0:
                sum_ += l*antall_løsninger(s[t+tall[i]+1:], tall[i+1:])
    return sum_

def rek_perms(split, tall, r):
    if len(tall) == 0:
        if any(("#" in e for e in split)):
            return 0
        else:
            return 1
            
    s = 0
    for i in range(len(tall)+1):
        if sum(tall[:i])+len(tall[:i])-1 > len(split[0]):
            continue
        if sum(tall[i:])+len(tall[i:])-1 > sum(len(st) for st in split[1:])+len(split[1:])-1:
            continue

        l = antall_løsninger(split[0], tall[:i])
        
        if l > 0:
            s += l*rek_perms(split[1:], tall[i:], r+2)

    return s

sum_ = 0
for i,(s,antall) in enumerate(linjer):
    s = '?'.join(5*[s])
    tall = 5*[int(e) for e in antall.split(",")]
    s,tall = min((s,tall),(s[::-1], tall[::-1]))

    split = [e for e in s.split(".") if e != '']
    sum_ += rek_perms(split, tall, 1)

print(sum_)
# 33992866292225