import re
from collections import defaultdict

formulas      = {}
with open('inputs/14', 'r') as f:
    for line in f:
        lhs, rhs = line.split('=>')[0], line.split('=>')[1].strip()
        formulas[rhs] = lhs.split(',')

def evaluate_cost(s, res):
    s_= re.split('(\d+)',s.strip())
    num, mat = s_[1], s_[2]

    # base case
    if 'ORE' in mat:
        return int(num)
    # induction step 1
    elif int(num) <= res[mat]:
        return 0
    # induction step n+1
    else:
        cost = 0
        for k, v in formulas.items():
            if mat in k: # then v is a list of what we need
                # how much do we actually get?
                num_we_get = re.split('(\d+)', k.strip())[1]
                for vv in v: # e.g ['7 A', '1 E']
                    cost += evaluate_cost(vv, res) # '7A'
                    res[mat] += int(num_we_get)


        #cost = [evaluate_cost(i, res) for i in [v for k, v in formulas.items() if mat in k][0]]
        return cost

res = defaultdict(lambda: 0)

print(evaluate_cost('1 FUEL',res))
s
