# løst

with open("2025/11.txt","r") as f:
    treehash = {e.split(": ")[0]: e.rstrip("\n").split(" ",1)[1].split(" ") for e in f.readlines()}


def treesøk(k):
    if k == "out":
        return 1
    return sum(treesøk(v) for v in treehash[k]) 

print(treesøk("you"))
# 574