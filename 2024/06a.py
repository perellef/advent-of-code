# løst

with open("2024/06.txt","r") as f:
    matrise = [e.rstrip("\n") for e in f.readlines()]

pos = [(r,k) for r in range(len(matrise)) for k in range(len(matrise[0])) if matrise[r][k] == "^"][0]
retning = (-1,0)

rotasjon = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0)
}

besøkt = set()
while True:
    r,k = pos
    besøkt.add(pos)

    if any((
        r == 0,
        k == 0,
        r == len(matrise)-1,
        k == len(matrise[0])-1
    )):
        break

    r_ny = r+retning[0]
    k_ny = k+retning[1]

    if matrise[r_ny][k_ny] == "#":
        retning = rotasjon[retning]
    else:
        pos = (r_ny, k_ny)

print(len(besøkt))
# 5101