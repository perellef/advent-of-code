# løst

with open("2025/02.txt","r") as f:
    linjer = ''.join([e.rstrip("\n") for e in f.readlines()])


ranges = [e.split("-") for e in linjer.split(",")]

s = 0
for a,b in ranges:

    invalids = set()
    
    for n in range(2,len(b)+1):
        tall = 0 if len(a) < n else int(a[:(len(a)//n)])
        
        while True:
            inv = int(n * str(tall))
            if inv > int(b):
                break
            
            if inv >= int(a):
                invalids.add(inv)
            tall += 1

    for inv in invalids:
        s += inv

print(s)
# 54446379122