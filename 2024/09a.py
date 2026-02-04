# løst

with open("2024/09.txt","r") as f:
    diskplass = [e.rstrip("\n") for e in f.readlines()][0]

disk = lambda x: int(diskplass[x])

utplassert = []

v = 0
h = len(diskplass)-1
verdi_v, verdi_h = disk(v), disk(h)

while v <= h:

    if v == h:
        utplassert.append((v//2, min(verdi_h, verdi_v)))
        break

    if v % 2 == 0:
        utplassert.append((v//2, disk(v)))
        v += 1
        verdi_v = disk(v)
        continue

    if verdi_v < verdi_h:
        verdi_h -= verdi_v  
        utplassert.append((h//2, verdi_v))
        v += 1
        verdi_v = disk(v)
        continue
    
    if verdi_v == verdi_h:
        utplassert.append((h//2, verdi_h))
        v += 1
        h -= 2
        verdi_h = disk(h)
        verdi_v = disk(v)
        continue

    if verdi_v > verdi_h:
        verdi_v -= verdi_h  
        utplassert.append((h//2, verdi_h))
        h -= 2
        verdi_h = disk(h)
        continue


i = 0
s = 0
for (v,n) in utplassert:
    for _ in range(n):
        s += i*v
        i += 1

print(s)
# 6216544403458