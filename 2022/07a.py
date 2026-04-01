# løst

with open("2022/07.txt","r") as f:
    linje = [e.rstrip("\n") for e in f.readlines()]

for i in range(len(linje)-3):
    if len(set(linje[i:i+4])) == 4:
        print(i+4)
        break
# 1282