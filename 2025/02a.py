# løst

with open("2025/02.txt","r") as f:
    linjer = ''.join([e.rstrip("\n") for e in f.readlines()])

ranges = [e.split("-") for e in linjer.split(",")]

s = 0
for a,b in ranges:

    invalids = set()
    
    tall = 0 if len(a) < 2 else int(a[:(len(a)//2)])
    
    while True:
        inv = int(2 * str(tall))
        if inv > int(b):
            break
        
        if inv >= int(a):
            invalids.add(inv)
        tall += 1

    for inv in invalids:
        s += inv

print(s)
# 32976912643
