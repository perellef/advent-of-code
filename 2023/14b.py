# løst

with open("2023/14.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

def transpose(m):
    return [''.join(m[r][k] for r in range(len(m))) for k in range(len(m[0]))]

def tilt(m, direction):
    f1 = lambda x: x
    f2 = lambda x: x
    reverse = False

    if direction in "SN":
        f1 = lambda x: transpose(x)
        f2 = lambda x: transpose(x)
    if direction in "NW":
        reverse = True

    return f2(['#'.join([''.join(sorted(el, reverse=reverse)) for el in e.split("#")]) for e in f1(m)])

def vekt(m):
    s = 0
    for e in transpose(m):
        for i,char in enumerate(reversed(e), start=1):
            if char == "O":
                s += i
    return s


N = 1000000000

besøkt = {}
i = 0
while i < N:
    besøkt['\n'.join(matrise)] = i
    
    if i % 1000 == 0:
        print(i, vekt(matrise))

    før = matrise
    for direction in "NWSE":
        matrise = tilt(matrise, direction)
    
    i += 1
    
    if '\n'.join(matrise) in besøkt:
        delta = i-besøkt['\n'.join(matrise)]
        if (N-i) % delta == 0:
            break

print(vekt(matrise))
# 96061