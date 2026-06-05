# løst

with open("2023/14.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

def transpose(m):
    return [''.join(m[r][k] for r in range(len(m))) for k in range(len(m[0]))]

def tilt(m, direction):
    f = lambda x: transpose(x) if direction in "SN" else x
    reverse = direction in "NW"

    return f(['#'.join(''.join(sorted(el, reverse=reverse)) for el in e.split("#")) for e in f(m)])

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

    for direction in "NWSE":
        matrise = tilt(matrise, direction)
    
    i += 1
    if '\n'.join(matrise) in besøkt:
        delta = i-besøkt['\n'.join(matrise)]
        if (N-i) % delta == 0:
            break

print(vekt(matrise))
# 96061