# løst

N = 70
NUM_BYTES = 1024

with open("2024/18.txt","r") as f:
    corruptions = [(int(e.rstrip("\n").split(",")[0]), int(e.rstrip("\n").split(",")[1])) for e in f.readlines()]

def blokkerer_løsning(i):  

    corruptions_i = corruptions[:i]

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
                return False
            if min(n) < 0 or max(n) > N:
                continue
            if n in besøkt:
                continue
            if n in corruptions_i:
                continue
            besøkt.add(n)

            nye_neste.append((n[0]+1,n[1]))
            nye_neste.append((n[0]-1,n[1]))
            nye_neste.append((n[0],n[1]+1))
            nye_neste.append((n[0],n[1]-1))

        if len(neste) == 0:
            return True

        neste = nye_neste

for i in range(len(corruptions)+1):
    if blokkerer_løsning(i):
        print(f"{corruptions[i-1][0]},{corruptions[i-1][1]}")
        break

# 45,18  615.783s
