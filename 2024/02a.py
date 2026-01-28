# løst

with open("2024/02.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

def er_safe(lst):
    if not any((
        lst == list(sorted(lst)),
        lst == list(sorted(lst, reverse=True))
    )):
        return False

    if len(set(lst)) != len(lst):
        return False

    for i in range(len(lst)-1):
        if abs(lst[i]-lst[i+1]) > 3:
            return False
    return True


s = 0
for linje in linjer:
    lst = [int(el) for el in linje.split(" ")]

    s += int(er_safe(lst))
print(s)
# 369