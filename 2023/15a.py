# løst
with open("2023/15.txt","r") as f:
    hashord = f.readlines()[0]

def hash(s):
    h = 0
    for t in s:
        h += ord(t)
        h *= 17
        h %= 256
    return h

sum_ = 0
for s in hashord.split(","):
    sum_ += hash(s)
print(sum_)

# 515495