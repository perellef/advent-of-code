# løst

with open("2024/11.txt","r") as f:
    steiner = [e.rstrip("\n").split(" ") for e in f.readlines()][0]

for _ in range(25):
    nye_steiner = []
    for stein in steiner:
        if stein == "0":
            nye_steiner.append("1")
        elif len(stein) % 2 == 0:
            ny_stein1 = stein[:len(stein)//2]
            ny_stein2 = stein[len(stein)//2:]
            nye_steiner.append(ny_stein1)
            nye_steiner.append(ny_stein2[:-1].lstrip("0") + ny_stein2[-1])
        else:
            nye_steiner.append(str(int(stein)*2024))

    steiner = nye_steiner
print(len(steiner))

# 183435