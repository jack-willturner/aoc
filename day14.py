import re

formulas = {}
with open('things.txt', 'r') as f:
    for line in f:
        lhs, rhs = line.split('=>')[0], line.split('=>')[1].strip()
        formulas[rhs] = lhs.split(',')

def evaluate_cost(s):
    s_= re.split('(\d+)',s.strip())
    num, mat = s_[1], s_[2]
    
    if 'ORE' in mat:
        return 1
    else:
        return sum([evaluate_cost(i) for i in [v for k, v in formulas.items() if mat in k][0]])

print(formulas)
print(evaluate_cost('1 FUEL'))
