
with open("2024/09.txt","r") as f:
    diskplass = [e.rstrip("\n") for e in f.readlines()][0]

utplassert = [((i,int(v)) if i%2==0 else (None, int(v))) for i,v in enumerate(diskplass)]+[(None,0)]


i = len(utplassert)-2
while i >= 0:
    mindre = False
    for l in range(1, i, 2):
        if utplassert[l][1] >= utplassert[i][1]:
            utplassert[l] = (None, utplassert[l][1]-utplassert[i][1])
            utplassert.insert(l, utplassert[i])
            utplassert.insert(l, (None, 0))
            
            utplassert[i+1] = (None, utplassert[i+1][1]+utplassert[i+2][1]+utplassert[i+3][1])
            utplassert.pop(i+2)
            utplassert.pop(i+2)
            mindre = True

    if not mindre: 
        i -= 2


i = 0
s = 0
for v,k in utplassert:
    for _ in range(k):
        if v != None:
            s += i * (v//2)
        i += 1
print(s)

