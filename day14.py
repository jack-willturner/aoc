import re
from collections import defaultdict
import time

formulas      = {}
with open('inputs/14', 'r') as f:
    for line in f:
        lhs, rhs = line.split('=>')[0], line.split('=>')[1].strip()
        formulas[rhs] = lhs.split(',')

print(formulas)

def evaluate_cost(s, res):

    print(s, res)
    time.sleep(1)
    s_= re.split('(\d+)',s.strip())
    num, mat = int(s_[1]), s_[2]

    # base case
    if 'ORE' in mat:
        return num, res
    # induction step 1
    elif num <= res[mat]:
        res[mat] = res[mat] - num
        return 0, res
    # induction step n+1
    else:
        cost = 0
        for k, v in formulas.items():
            if mat in k: # then v is a list of what we need
                not_enough = True
                running_tot = 0
                while(not_enough):
                    # how much do we actually get?
                    num_we_get = re.split('(\d+)', k.strip())[1]
                    running_tot += int(num_we_get)
                    for vv in v: # e.g ['7 A', '1 E']
                        c, res = evaluate_cost(vv, res)
                        cost += c

                    if running_tot >= num:
                        not_enough = False
                        print(running_tot - num)
                        res[mat] += running_tot - num # - num_we_need
        print()
        return cost, res

res = defaultdict(lambda: 0)
print()
print(evaluate_cost('1 FUEL',res))
