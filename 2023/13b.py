# løst

with open("2023/13.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

linjer = [e.split("|") for e in '|'.join(linjer).split("||")]

def er_en_unna(s1,s2):
    return sum(1 for c1,c2 in zip('|'.join(s1),'|'.join(s2)) if c1 != c2) == 1


s = 0
for pattern in linjer:

    horisontal = pattern
    vertikal = [''.join(pattern[r][k] for r in range(len(pattern))) for k in range(len(pattern[0]))]

    for i in range(1,len(horisontal)):
        n = min(i, len(horisontal)-i)
        if er_en_unna(horisontal[i-n:i], horisontal[i+n-1:i-1:-1]):
            s += 100*i

    for i in range(1,len(vertikal)):
        n = min(i, len(vertikal)-i)
        if er_en_unna(vertikal[i-n:i], vertikal[i+n-1:i-1:-1]):
            s += i

print(s)
# 32728