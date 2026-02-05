# løst

with open("2024/13.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

# Button A
# Button B

# i. x = na*ax + nb*bx
# ii. y = na*ay + nb*by

# (ii) na = (y - nb*by)/ay
# (i)  x = ((y - nb*by)/ay)*ax + nb*bx
# <=> x = y*ax/ay - nb*by*ax/ay + nb*bx
# <=> x = y*ax/ay + nb*(bx - by*ax/ay)
# <=> x-y*ax/ay = nb*(bx - by*ax/ay)
# <=> nb = (x-y*ax/ay)/(bx - by*ax/ay)

nb = lambda x,y,ax,ay,bx,by: round((x-y*ax/ay)/(bx - by*ax/ay))
na = lambda y, nb, by, ay: round((y - nb*by)/ay)

EKSTRA = 10000000000000

s = 0
for i in range(0, len(inp), 4):
    ax = int(inp[i].split(", ")[0].split("+")[-1].split("-")[-1])
    ay = int(inp[i].split(", ")[1].split("+")[-1].split("-")[-1])
    bx = int(inp[i+1].split(", ")[0].split("+")[-1].split("-")[-1])
    by = int(inp[i+1].split(", ")[1].split("+")[-1].split("-")[-1])

    x = int(inp[i+2].split(", ")[0].split("=")[-1]) + EKSTRA
    y = int(inp[i+2].split(", ")[1].split("=")[-1]) + EKSTRA

    n_b = nb(x,y,ax,ay,bx,by)
    n_a = na(y, n_b, by, ay)

    if n_a*ax + n_b*bx == x and n_a*ay + n_b*by == y:
        s += n_a*3+n_b

print(s)
# 104958599303720