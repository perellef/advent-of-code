# løst

with open("2024/22.txt","r") as f:
    inp = [int(e.rstrip("\n")) for e in f.readlines()]

def neste(secret):
    a = secret * 64
    secret ^= a
    secret %= 16777216

    b = secret // 32
    secret ^= b
    secret %= 16777216

    c = secret * 2048
    secret ^= c
    secret %= 16777216

    return secret

s = 0
for secret in inp:
    for _ in range(2000):
        secret = neste(secret)
    s += secret
print(s)
# 19822877190
