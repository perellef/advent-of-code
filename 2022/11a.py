# løst

with open("2022/11.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

aper = [e.split("\n") for e in '\n'.join(linjer).split("\n\n")]

aper_parset = {}
for ape in aper:
    apenr = int(ape[0].removeprefix("Monkey ")[:-1])
    items = [int(e) for e in ape[1].removeprefix("  Starting items: ").split(",")]
    
    operasjon = lambda old: eval(ape[2].replace("old", str(old)))
    sjekk_divisible_by = int(ape[3].removeprefix("  Test: divisible by "))
    if_true_apenr = int(ape[4].removeprefix("    If true: throw to monkey "))
    if_false_apenr = int(ape[5].removeprefix("    If false: throw to monkey "))

    aper_parset[apenr] = {
        "items": items,
        "operasjon": ape[2].removeprefix("  Operation: new = "),
        "sjekk-divisible-by": sjekk_divisible_by,
        "if": {
            True: if_true_apenr,
            False: if_false_apenr,
        }
    }

inspeksjoner = [0 for _ in aper]

for _ in range(20):
    for i in range(len(aper)):
        inspeksjoner[i] += len(aper_parset[i]["items"])
        for item in aper_parset[i]["items"][:]:
            ny = eval(aper_parset[i]["operasjon"].replace("old", str(item))) // 3
            nestemann = aper_parset[i]["if"][ny % aper_parset[i]["sjekk-divisible-by"] == 0]

            aper_parset[i]["items"].remove(item)
            aper_parset[nestemann]["items"].append(ny)

mest = list(sorted(inspeksjoner, reverse=True))

print(mest[0]*mest[1])
# 58056