# løst

with open("2024/15.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

skille = inp.index("")

kart = [list(e) for e in inp[:skille]]
instrukser = ''.join(inp[skille+1:])

retninger = {
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1),
}


pos = [(r,k) for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "@"][0]
for instruks in instrukser:
    r,k = pos
    dr,dk = retninger[instruks]
    
    ny_r,ny_k = r+dr, k+dk

    if kart[ny_r][ny_k] == "#":
        pos = r,k
    elif kart[ny_r][ny_k] == "O":

        O_r,O_k = ny_r,ny_k
        while True:
            O_r, O_k = O_r+dr, O_k+dk

            if kart[O_r][O_k] == "#":
                pos = r,k
                break
            
            if kart[O_r][O_k] == ".":
                kart[O_r][O_k] = "O"
                kart[r][k] = "."
                kart[ny_r][ny_k] = "@"
                pos = ny_r,ny_k
                break
    else:
        kart[ny_r][ny_k] = "@"
        kart[r][k] = "."
        pos = ny_r,ny_k

print(sum(100*r+k for k in range(len(kart[0])) for r in range(len(kart)) if kart[r][k] == "O"))
# 1360570
                  