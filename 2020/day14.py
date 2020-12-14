from collections import namedtuple
from itertools import product

Instruction = namedtuple('Instruction', 'mem value')

ls = []
with open("inputs/day14") as f:
    for line in f:
        line = line.replace('\n','').split('=')
        ls.append(Instruction(line[0].strip(), line[1].strip()))

## PART 1
mem = {}
for instr in ls:
    if 'mask' in instr.mem:
        mask = instr
    else:
        loc = int(instr.mem.split('[')[1].split(']')[0])
        mem[loc] = int(''.join([b if m=='X' else m for m, b in zip(mask.value, f"{int(instr.value):036b}")]),2)

print(sum(mem.values()))

## PART 2
def bitmask_addr(mask, addr):
    result = [b if m=='0' else m for m,b in zip(mask,f"{addr:036b}")]
    num_Xs = sum(1 if c =='X' else 0 for c in result)

    addresses = []
    for p in product([0,1], repeat=num_Xs):
        i = 0
        copy = []
        for j,c in enumerate(result):
            if c=='X':
                copy.append(str(p[i]))
                i += 1
            else:
                copy.append(c)
        
        addresses.append(''.join(copy))

    return addresses

mem = {}
for instr in ls:
    if 'mask' in instr.mem:
        mask = instr
    else:
        loc = int(instr.mem.split('[')[1].split(']')[0])
        addrs = bitmask_addr(mask.value, loc) ##
        for addr in addrs:
            loc = int(addr,2)
            mem[loc] = int(instr.value)

print(sum(mem.values()))