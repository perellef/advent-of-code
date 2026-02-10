# løst

with open("2024/24.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

i = inp.index("")

vals = {}
for val in inp[:i]:
    v,svar = val.split(": ")
    vals[v] = int(svar)

operator = {
    "XOR": (lambda x,y: x ^ y),
    "AND": (lambda x,y: x & y),
    "OR": (lambda x,y: x | y),
}

while len(vals) < len(inp)-1:
    for eq in inp[i+1:]:
        v1 = eq.split(" ")[0]
        op = eq.split(" ")[1]
        v2 = eq.split(" ")[2]
        ny_v = eq.split(" -> ")[1]

        if all((
            v1 in vals,
            v2 in vals,
            ny_v not in vals
        )): 
            vals[ny_v] = operator[op](vals[v1],vals[v2]) 

zs = int(''.join([str(v) for k,v in sorted(vals.items(), reverse=True) if k.startswith("z")]), 2)

print(zs)
# 51715173446832