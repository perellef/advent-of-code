from collections import defaultdict 

with open("05.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

# ==== 1a ====

spl = linjer.index("")

ranges_str = [(int(e.split("-")[0]),int(e.split("-")[1])) for e in linjer[:spl]]
available = linjer[spl+1:]

alle = []
def avail(x):
    for a,b in ranges_str:
        if a <= x and x <= b:
            alle.append(x)
            return
        
for x in available:
    avail(int(x))
print(len(alle))

# ==== 1b ====
ikkeoverlappende_ranges = []

def legg_til_range(a,b):
    for i in range(len(ikkeoverlappende_ranges)):
        r_a, r_b = ikkeoverlappende_ranges[i]

        if any((
            r_a <= a and a <= r_b+1,
            r_a-1 <= b and a <= r_b+1,
        )):
            ikkeoverlappende_ranges[i] = (min(r_a, a), max(r_b, b))
            return
    ikkeoverlappende_ranges.append((a, b))
    
for a,b in sorted(ranges_str):
    legg_til_range(a, b)

s = 0
for a,b in ikkeoverlappende_ranges:
    s += b-a+1

print(s)
# 334714395325710