# løst

with open("2022/09.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

besøkte = set()

head = (0,0)
tail = [(0,0) for _ in range(9)]
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
        

        if abs(tail[0][0]-nytt_hode[0]) > 1 or abs(tail[0][1]-nytt_hode[1]) > 1:
            tail[0] = head

        head = nytt_hode
            
        for i in range(8):
            if abs(tail[i+1][0]-tail[i][0]) == 2 and tail[i+1][1]-tail[i][1] == 0:
                tail[i+1] = (tail[i+1][0]+(tail[i][0]-tail[i+1][0])//2, tail[i+1][1])
            elif abs(tail[i+1][1]-tail[i][1]) == 2 and tail[i+1][0]-tail[i][0] == 0:
                tail[i+1] = (tail[i+1][0], tail[i+1][1]+(tail[i][1]-tail[i+1][1])//2)
            elif abs(tail[i+1][0]-tail[i][0]) + abs(tail[i+1][1]-tail[i][1]) > 2:
                tail[i+1] = (
                    tail[i+1][0]+(tail[i][0]-tail[i+1][0])//abs(tail[i][0]-tail[i+1][0]),
                    tail[i+1][1]+(tail[i][1]-tail[i+1][1])//abs(tail[i][1]-tail[i+1][1])
                )

        besøkte.add(tail[8])

print(len(besøkte))
# 2661