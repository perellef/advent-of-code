# løst 

with open("2023/06.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

ts = [int(e) for e in linjer[0].removeprefix("Time: ").split(" ") if e != '']
ds = [int(e) for e in linjer[1].removeprefix("Distance: ").split(" ") if e != '']

s = 1
for t,d in zip(ts,ds):
    c = 0
    for i in range(0,t+1):
        dis = i*(t-i)
        if dis > d:
            c += 1
    s *=c
    
print(s)
# 4568778