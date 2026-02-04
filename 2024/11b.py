# løst

with open("2024/11.txt","r") as f:
    inp = [e.rstrip("\n").split(" ") for e in f.readlines()][0]

from collections import defaultdict

steiner = defaultdict(int)
for k in inp:
    steiner[k] += 1

for i in range(75):
    nye_steiner = defaultdict(int)
    
    for stein,k in steiner.items():
        if stein == "0":
            nye_steiner["1"] += k
        elif len(stein) % 2 == 0:
            ny_stein1 = stein[:len(stein)//2]
            ny_stein2 = stein[len(stein)//2:]
            nye_steiner[ny_stein1] += k
            nye_steiner[ny_stein2[:-1].lstrip("0") + ny_stein2[-1]] += k
        else:
            nye_steiner[str(int(stein)*2024)] += k
    steiner = nye_steiner
print(sum(steiner.values()))

# 218279375708592