# løst

with open("2023/19.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

ws,ps  = ';'.join(linjer).split(";;")
parts = []
for p in ps.split(";"):
    parts.append((
        int((p.split("=")[1].split(",")[0])),
        int((p.split("=")[2].split(",")[0])),
        int((p.split("=")[3].split(",")[0])),
        int((p.split("=")[4].split("}")[0])),
    ))

index = {"x": 0, "m": 1, "a": 2, "s": 3}

def workflow(w):
    def f(t):
        for i in range(len(w.split(","))-1):
            cond,kode = w.split(",")[i].split(":")

            i = index[cond[0]]
            tall = int(cond[2:])
            if cond[1] == "<" and t[i] < tall:
                return kode
            if cond[1] == ">" and t[i] > tall:
                return kode
        return w.split(",")[-1]
    return f

workflows = {w.split("{")[0]: workflow(w.split("{")[1].rstrip("}")) for w in ws.split(";")}

def aksepteres(kode, t):
    ny_kode = workflows[kode](t)
    if ny_kode == "A":
        return True
    if ny_kode == "R":
        return False
    return aksepteres(ny_kode, t)

s = 0
for p in parts:
    if aksepteres("in", p):
        s += sum(p)

print(s)
# 476889