# løst

with open("2024/23.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

from collections import defaultdict

koblinger = defaultdict(set)

for el in inp:
    a,b = el.split("-")
    koblinger[a].add(b)
    koblinger[b].add(a)

grupper_3 = set()

for n1,v in koblinger.items():
    for n2 in v:
        for n3 in koblinger[n2]:
            if n3 in v:
                gruppe = tuple(sorted((n1,n2,n3)))
                grupper_3.add(gruppe)

grupper = list(grupper_3)
while True:
    la_til = False
    for i,gruppe in enumerate(grupper.copy()):
        for ny in koblinger[gruppe[0]]:
            if all(ny in koblinger[n] for n in gruppe):
                grupper[i] = tuple(sorted(list(gruppe) + [ny]))
                la_til = True
    if not la_til:
        break

    grupper = list(set(grupper))

største_gruppe = max(grupper, key=len)

print(','.join(største_gruppe))
# ag,gh,hh,iv,jx,nq,oc,qm,rb,sm,vm,wu,zr