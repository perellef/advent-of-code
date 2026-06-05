# løst

with open("2023/15.txt","r") as f:
    hashord = f.readlines()[0]

def hash(s):
    h = 0
    for t in s:
        h += ord(t)
        h *= 17
        h %= 256
    return h

bokser = [{} for _ in range(256)]

sum_ = 0
for s in hashord.split(","):
    kodeord = s.split("-")[0].split("=")[0]
    h = hash(kodeord)

    er_lik_tegn = ("=" in s)
    focal_size = None if not er_lik_tegn else int(s.split("=")[-1])

    if er_lik_tegn:
        bokser[h][kodeord] = focal_size
    else:
        if kodeord in bokser[h]: 
            del bokser[h][kodeord]

s = 0 
for i1,boks in enumerate(bokser, start=1):
    for i2,f in enumerate(boks.values(), start=1):
        s += i1*i2*f
print(s)
# 229349