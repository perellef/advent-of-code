with open("02.txt","r") as f:
    linjer = ''.join([e.rstrip("\n") for e in f.readlines()])

# === 1a ====
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

# === 1b ====

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