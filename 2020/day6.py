with open('inputs/day6','r') as f:
    inputs = f.read()

## PART 1
p1_inputs = [i.replace('\n','') for i in inputs.split('\n\n')]
print(sum([len(set(i)) for i in p1_inputs]))

## PART 2
from collections import defaultdict 

p2_inputs = inputs.split('\n\n')

num_val = 0
for inp in p2_inputs:
    num_people = inp.count('\n') + 1 
    i = inp.replace('\n','')
    
    freq_dict = defaultdict(lambda: 0)

    for char in i:
        freq_dict[char] += 1
    
    
    for k in freq_dict.keys():
        if freq_dict[k] == num_people:
            num_val += 1
    
print(num_val)