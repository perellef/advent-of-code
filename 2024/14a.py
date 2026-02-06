# løst

with open("2024/14.txt","r") as f:
    inp = [e.rstrip("\n") for e in f.readlines()]

posisjoner = []
B = 101
H = 103
N = 100

for e in inp:
    start_x = int(e.split(",")[0].split("=")[1])
    start_y = int(e.split(",")[1].split(" ")[0])
    
    ax = int(e.split("v=")[1].split(",")[0])
    ay = int(e.split("v=")[1].split(",")[1])

    x = (start_x+N*ax)%B
    y = (start_y+N*ay)%H

    posisjoner.append((x,y))

grupper = {
    (0,0): 0,
    (0,1): 0,
    (1,0): 0,
    (1,1): 0
}

for x,y in posisjoner:
    if x==(B-1)//2 or y==(H-1)//2:
        continue

    grupper[(int(x>(B-1)//2), int(y>(H-1)//2))] += 1

p = 1
for v in grupper.values():
    p *= v

print(p)
# 230900224    