# løst

with open("2022/06.txt","r") as f:
    linje = f.read()

for i in range(len(linje)-13):
    if len(set(linje[i:i+14])) == 14:
        print(i+14)
        break
# 3513