# løst

with open("2024/15.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

skille = inp.index("")

ekspander = {"@": "@.", "O": "[]", ".": "..", "#": "##"}

kart = [list(''.join(ekspander[t] for t in e)) for e in inp[:skille]]

instrukser = ''.join(inp[skille+1:])

retninger = {
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1),
}

def kan_flytte(r, k, dr, dk):
    if kart[r][k] == ".":
        return True
    if kart[r][k] == "#":
        return False
    
    if dk == 0:
        if kart[r][k] == "[":
            return kan_flytte(r+dr,k, dr, dk) and kan_flytte(r+dr,k+1, dr, dk)
        else:
            return kan_flytte(r+dr,k-1, dr, dk) and kan_flytte(r+dr,k, dr, dk)
    else:
        return kan_flytte(r,k+2*dk, dr, dk)

def flytt(tegn, r, k, dr, dk):
    if kart[r][k] == ".":
        kart[r][k] = tegn
        return
    if kart[r][k] == "#":
        raise ValueError("Skulle ikke ha kommet hit")
    
    if dk == 0:
        if kart[r][k] == "[":
            flytt(kart[r][k], r+dr,k, dr, dk)
            flytt(kart[r][k+1], r+dr,k+1, dr, dk)
            kart[r][k+1] = "."
        else:
            flytt(kart[r][k-1], r+dr,k-1, dr, dk)
            flytt(kart[r][k], r+dr,k, dr, dk)
            kart[r][k-1] = "."
    else:
        flytt(kart[r][k], r,k+dk, dr, dk)
    
    kart[r][k] = tegn

pos = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "@"][0]
for instruks in instrukser:
    r,k = pos
    dr,dk = retninger[instruks]
    
    ny_r,ny_k = r+dr, k+dk

    if kan_flytte(ny_r,ny_k,dr,dk):
        flytt("@", ny_r, ny_k, dr, dk)
        kart[r][k] = "."
        pos = ny_r,ny_k
            
print(sum(100*r+k for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "["))

# 1381446     