# løst 

import math

with open("2023/06.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

t = int(''.join(linjer[0].removeprefix("Time: ").split(" ")))
d = int(''.join(linjer[1].removeprefix("Distance: ").split(" ")))

x1 = t+(t**2-4*d)**(1/2)/2 - 1e-4
x2 = t-(t**2-4*d)**(1/2)/2 + 1e-6
    
print(math.floor(x1)-math.ceil(x2))
# 28973936