# løst
with open("2022/09.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

besøkte = set()

head = (0,0)
tail = (0,0)
for linje in linjer:
    d,n = linje.split()
    for _ in range(int(n)):

        if d == "U":
            nytt_hode = (head[0]+1, head[1])
        elif d == "D":
            nytt_hode = (head[0]-1, head[1])
        elif d == "R":
            nytt_hode = (head[0], head[1]+1)
        elif d == "L":
            nytt_hode = (head[0], head[1]-1)
        else:
            raise ValueError
        
        if abs(tail[0]-nytt_hode[0]) > 1 or abs(tail[1]-nytt_hode[1]) > 1:
            tail = head
        
        head = nytt_hode
        besøkte.add(tail)

print(len(besøkte))
# 6284