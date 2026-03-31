# løst

with open("2022/01.txt","r") as f:
    linjer = f.read()

grupper = [sum(map(int, e.split('\n'))) for e in linjer.split("\n\n")]

print(sum(list(sorted(grupper, reverse=True))[:3]))
# 203002