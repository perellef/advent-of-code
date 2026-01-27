# løst

with open("2025/09.txt","r") as f:
    koords = [(int(e.split(",")[0]),int(e.split(",")[1].rstrip("\n"))) for e in f.readlines()]

kanter = []
x_sorted = list(sorted(koords))
y_sorted = list(sorted(koords, key=lambda x: (x[1], x[0])))
for i in range(0,len(koords),2):
    kanter.append((x_sorted[i], x_sorted[i+1]))
    kanter.append((y_sorted[i], y_sorted[i+1]))

def er_gyldig(x1,y1,x2,y2):
    for fra,til in kanter:
        # overlapper i x-akse
        if max(min(x1,x2), min(fra[0], til[0])+1) <= min(max(fra[0], til[0])-1, max(x1,x2)) and min(y1,y2) < fra[1] and fra[1] < max(y1,y2):
            return False
        
        # overlapper i y-akse
        if max(min(y1,y2), min(fra[1], til[1])+1) <= min(max(fra[1], til[1])-1, max(y1,y2)) and min(x1,x2) < fra[0] and fra[0] < max(x1,x2):
            return False
    return True

m = 0
for x1,y1 in koords:
    for x2,y2 in koords:
        if er_gyldig(x1,y1,x2,y2):
            m = max(m, (abs(x2-x1)+1)*(abs(y2-y1)+1))
print(m)
# 1498673376, 186.978s