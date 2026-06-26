# løst

N = 70
NUM_BYTES = 1024

with open("2024/18.txt","r") as f:
    corruptions = set([(int(e.rstrip("\n").split(",")[0]), int(e.rstrip("\n").split(",")[1])) for e in f.readlines()][:NUM_BYTES])

def beregn_antall_steg():    
    start = (0,0)
    slutt = (N,N)

    besøkt = set()
    neste = [start]

    steg = -1
    while True:
        steg += 1

        nye_neste = []
        for n in neste:
            if n == slutt:
                return steg
            if min(n) < 0 or max(n) > N:
                continue
            if n in besøkt:
                continue
            if n in corruptions:
                continue
            besøkt.add(n)

            nye_neste.append((n[0]+1,n[1]))
            nye_neste.append((n[0]-1,n[1]))
            nye_neste.append((n[0],n[1]+1))
            nye_neste.append((n[0],n[1]-1))

        neste = nye_neste

print(beregn_antall_steg())
# 316
