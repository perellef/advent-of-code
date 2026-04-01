# løst

with open("2022/05.txt","r") as f:
    linjer = [e.rstrip("\n") for e in f.readlines()]

bokser = linjer[:linjer.index("")]
kommandoer = linjer[linjer.index("")+1:]

stacks = []
for i in range(1, len(bokser[-1]), 4):
    stacks.append([])

for b in reversed(range(len(bokser)-1)):
    for s,i in enumerate(range(1, len(bokser[b]), 4)):
        if bokser[b][i] != " ":
            stacks[s].append(bokser[b][i])

for kommando in kommandoer:
    antall = int(kommando.split("move ")[1].split(" from")[0])
    fra = int(kommando.split(" from ")[1].split(" to ")[0])-1
    til = int(kommando.split(" to ")[1])-1
    stacks[til], stacks[fra] = stacks[til]+stacks[fra][-antall:], stacks[fra][:-antall]

print(''.join(map(lambda x: x[-1], stacks)))
# LCTQFBVZV