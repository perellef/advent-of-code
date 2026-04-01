# løst

with open("2022/06.txt","r") as f:
    linje = f.read()

for i in range(len(linje)-3):
    if len(set(linje[i:i+4])) == 4:
        print(i+4)
        break
# 1282