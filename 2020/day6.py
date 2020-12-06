with open('inputs/day6','r') as f:
    inputs = f.read()

## PART 1
p1_inputs = [i.replace('\n','') for i in inputs.split('\n\n')]
print(sum([len(set(i)) for i in p1_inputs]))

## PART 2 
p2_inputs = [i.split('\n') for i in inputs.split('\n\n')]
p2_sets = [[set(i) for i in inp] for inp in p2_inputs]
print(sum([len(set.intersection(*s)) for s in p2_sets]))