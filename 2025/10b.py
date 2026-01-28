import heapq

with open("2025/10.txt","r") as f:
    linjer = [e.split(" ") for e in f.readlines()]

def raskeste(joltage, knapper):

    def ny_joltage(gammel, i, k):
        ny_n = list(gammel)
        for indeks in knapper[i]:
            ny_n[indeks] -= k
        return ny_n

    ns = [(0, sum(joltage), joltage, [])]

    while True:
        minsteg,s,jolt,ks = heapq.heappop(ns)
        print(minsteg, f"{len(ks)}/{len(knapper)}", len(ns))

        gj = sum(jolt)
        steg = len(knapper[len(ks)])

        if len(ks) == len(knapper) - 1:
            k = gj//steg
            ny = ny_joltage(jolt, len(ks), k)
            if min(ny) < 0:
                continue
            if max(ny) == 0:
                return sum(ks+[k])
            continue
            
        for tot in range(0, gj+1, steg):
            k = tot//steg
            ny = ny_joltage(jolt, len(ks), k)
            if min(ny) < 0:
                break
            heapq.heappush(ns, (sum(ks)+k+((gj-1)//len(knapper[len(ks)+1])), s-tot, ny, ks+[k]))


s = 0
for i,linje in enumerate(linjer):
    joltage = tuple(int(e) for e in linje[-1].lstrip("{").rstrip("}\n").split(","))
    knapper = [[int(el) for el in e.lstrip("(").rstrip(")").split(",")] for e in linje[1:-1]]
    
    knapper = sorted(knapper, key=lambda x: len(x), reverse=True)
    s += raskeste(joltage, knapper)
    print(s)
print(s)