# løst
 
with open("2025/09.txt","r") as f:
    koords = [(int(e.split(",")[0]),int(e.split(",")[1].rstrip("\n"))) for e in f.readlines()]


laveste_topp = None
laveste_venstre = None

topp_venstre = []

for x,y in sorted(koords):
    if laveste_venstre is None:
        laveste_topp = x
        laveste_venstre = y
        topp_venstre.append((x,y))
        continue

    if x < laveste_topp or y < laveste_venstre:
        laveste_topp = min(x, laveste_topp)
        laveste_venstre = min(y, laveste_venstre)

        topp_venstre.append((x,y))

laveste_bunn = None
laveste_høyre = None
bunn_høyre = []

for x,y in sorted(koords, reverse=True):

    if laveste_bunn is None:
        laveste_bunn = x
        laveste_høyre = y
        bunn_høyre.append((x,y))
        continue
    if x > laveste_bunn or y > laveste_høyre:
        laveste_topp = min(x, laveste_topp)
        laveste_venstre = min(y, laveste_venstre)

        bunn_høyre.append((x,y))

m = 0
for (x1,y1) in topp_venstre:
    for (x2,y2) in bunn_høyre:
        m = max(m, (x2-x1+1)*(y2-y1+1))

print(m)