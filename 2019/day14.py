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
    #time.sleep(1)
    s_= re.split('(\d+)',s.strip())
    num, mat = int(s_[1]), s_[2].strip()

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

            if mat == k[-(len(mat)):]: # then v is a list of what we need

                not_enough = True
                running_tot = 0
                while(not_enough):
                    
                    # how much do we actually get?
                    num_we_get = re.split('(\d+)', k.strip())[1]

                    running_tot += int(num_we_get)
                    for vv in v:
                        c, res = evaluate_cost(vv, res)
                        #res[mat] += num_we_get
                        cost += c

                    if running_tot >= num:
                        not_enough = False
                        if running_tot > int(num_we_get):
                            res[mat] += int(num_we_get)
                        else:
                            res[mat] += int(num_we_get) - num
        return cost, res

res = defaultdict(lambda: 0)

print(evaluate_cost('1 FUEL',res))
