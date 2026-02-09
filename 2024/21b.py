# løst

with open("2024/21.txt","r") as f:
    koder = [e.rstrip("\n") for e in f.readlines()]

def utled_låsstier(lås):
    knapper = [knapp for rad in lås for knapp in rad]
    låsstier = {}

    for k1 in knapper:
        for k2 in knapper:
            if "x" in (k1, k2):
                continue
            
            låsstier[k1+k2] = []

            startpos = [(x,y) for y,rad in enumerate(lås) for x in range(len(rad)) if lås[y][x] == k1][0]

            stier = [(startpos, "", set())]
            while stier:
                (x,y), sti, besøkte = stier.pop()

                if x < 0 or x == len(lås[0]) or y < 0 or y == len(lås):
                    continue

                if lås[y][x] == "x":
                    continue
                if len(besøkte) != len(sti):
                    continue
                if lås[y][x] == k2:
                    låsstier[k1+k2].append(sti+"A")
                    continue

                ny_besøkte = besøkte.union((lås[y][x],))

                stier.append(((x-1,y), sti+"<", ny_besøkte))
                stier.append(((x+1,y), sti+">", ny_besøkte))
                stier.append(((x,y-1), sti+"^", ny_besøkte))
                stier.append(((x,y+1), sti+"v", ny_besøkte))
    return låsstier

def utled_navigasjonstrykk(sekvens, num):
    d = {}
    d[1] = {sekv: min(map(len, l)) for sekv,l in sekvens.items()}

    for n in range(2,num+1):
        d[n] = {}

        for sekv,l in sekvens.items():
            s = 10000000000000000000
            for ny_sekv in l:
                s = min(s, kalkuler_knappetrykk(d, n-1, "A"+ny_sekv))
            d[n][sekv] = s
    return d

kalkuler_knappetrykk = lambda d, n, s: sum(d[n][s[i:i+2]] for i in range(len(s)-1))

N = 25

numlock = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["x", "0", "A"]
]
pilknapper = [
    ["x", "^", "A"],
    ["<", "v", ">"]
]

sekvenser = utled_låsstier(pilknapper)
navigasjonstrykk = utled_navigasjonstrykk(sekvenser, N)

numlockstier = utled_låsstier(numlock)


tot = 0
for kode in koder:
    A_kode = "A" + kode
    s = 0
    for i in range(len(A_kode)-1):
        stier = [e for e in numlockstier[A_kode[i:i+2]]]
        s += min(kalkuler_knappetrykk(navigasjonstrykk, N, "A"+sti) for sti in numlockstier[A_kode[i:i+2]])
    
    tot += s*int(kode.rstrip("A"))

print(tot)

# 245881705840972