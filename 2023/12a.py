# løst

with open("2023/12.txt","r") as f:
    linjer = [e.rstrip("\n").split(" ") for e in f.readlines()]

def er_gyldig(s, tall):
    subs = (s+".").split("?")
    antall = [len(e) for e in subs[0].split(".")[:-1] if len(e) > 0]

    if len(subs) == 1:
        return antall == tall
    return antall == tall[:len(antall)]

sum_ = 0
for i,(s,antall) in enumerate(linjer):
    antall = [int(e) for e in antall.split(",")]
    
    usikre = [i for i in range(len(s)) if s[i] == "?"]
    perms = [s]

    for u in usikre:
        ny_perms = []
        for p in perms:
            if not er_gyldig(p, antall):
                continue
            ny_perms.append(p[:u]+"."+p[u+1:])
            ny_perms.append(p[:u]+"#"+p[u+1:])
        perms = ny_perms

    sum_ += len([e for e in perms if er_gyldig(e, antall)])
    
print(sum_)
# 7195
