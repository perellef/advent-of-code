# løst

with open("2025/12.txt","r") as f:
    treehash = [e.rstrip("\n") for e in f.readlines()]

minst = {0: 7, 1: 6, 2: 7, 3: 5, 4: 7, 5: 7}

s = 0
for el in treehash:
    if "x" not in el:
        continue
    
    areal, gaver = el.split(": ")
    gaver = [int(e) for e in gaver.split(" ")]

    b = int(areal.split("x")[0])
    h = int(areal.split("x")[1])

    minimumsareal = sum([minst[i]*v for i,v in enumerate(gaver)])

    # tilgjengelig areal mindre enn antall formenes areal
    if minimumsareal > b*h:
        continue
    
    minst_antall_former = (b//3)*(h//3)
    if minst_antall_former >= sum(gaver):
        s += 1
        continue

    raise ValueError("Feil antakelse. Skulle ikke kunne ha nådd hit")
    # Ingen når hit.

    # Oppgaven er en lureoppgave fordi vi slipper å plassere noen former, for å løse oppgaven. Vi kan
    # simpelten sjekke at alle formene har større areal enn det tilgjengelige, eller se at alle formene
    # kan plasseres i sin 3x3 rute. 


print(s)
# 546



