# løst

with open("2025/10.txt","r") as f:
    linjer = [e.split(" ") for e in f.readlines()]

def raskeste(brytere, knapper):
    ns = [0]
    besøkt = set((0,))
    i = 1
    while True:
        ny_ns = []
        for n in ns:
            for knapp in knapper:
                ny_n = n ^ knapp
                if ny_n in besøkt:
                    continue
                besøkt.add(ny_n)

                if ny_n == brytere:
                    return i
                ny_ns.append(ny_n)

        ns = ny_ns
        i += 1

s = 0
for linje in linjer:
    brytere = int(''.join(["1" if switch == "#" else "0" for switch in reversed(linje[0].lstrip("[").rstrip("]"))]),2)

    knapper = [[int(el) for el in e.lstrip("(").rstrip(")").split(",")] for e in linje[1:-1]]
    knapper = [int(''.join(['1' if i in knapp else '0' for i in range(knapp[-1],-1,-1)]),2) for knapp in knapper]

    s += raskeste(brytere, knapper)
print(s)