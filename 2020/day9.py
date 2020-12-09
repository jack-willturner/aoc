from itertools import combinations

list = []
with open('inputs/day9','r') as f:
    for line in f:
        list.append(int(line))

## PART 1
preamble = 25

for i, digit in enumerate(list[preamble:]):
    
    sums = []
    for combination in combinations(list[i:preamble+i],2):
        sums.append(sum(combination))

    if not(digit in sums):
        invalid_num = digit
        break

print(invalid_num)

def sum_contig(list,i,j):
    contig = list[j:j+i]
    return sum(contig) 

## PART 2
broken = False
i = 2
while not broken:
    for j, digit in enumerate(list):
        contig = list[j:j+i]
        if sum(contig) == invalid_num:
            min_, max_ = min(contig), max(contig)
            broken = True
    i += 1

print(min_+max_)

