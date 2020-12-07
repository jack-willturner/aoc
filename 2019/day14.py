import queue
from math import ceil
import numpy as np
from collections import defaultdict

formulas      = {}
with open('inputs/14', 'r') as f:
    for line in f:
        lhs, rhs = line.split('=>')[0].strip(), line.split('=>')[1].strip()
        formulas[rhs] = lhs.split(',')

formula_fetcher = {k.split(' ')[1]:k for k in formulas.keys()} # e.g. 'A' : '2 A' -> the key in the formula dict

def splitstr(s):
    s = s.strip()
    return int(s.split(' ')[0]), s.split(' ')[1]

def eval(chem, amount):
    inventory = defaultdict(lambda : 0)    
    reactions = queue.LifoQueue()
    reactions.put({"chem": chem, "amount": amount})

    ore_needed = 0

    while(not reactions.empty()):
        r = reactions.get()
        
        if 'ORE' in r['chem']:
            ore_needed += r['amount']
        elif r['amount'] <= inventory[r['chem']]:
            inventory[r['chem']] -= r['amount']
        else:
            formula   = formula_fetcher[r['chem']]
            reactants = formulas[formula]

            amount_out, chemical_out = splitstr(formula)
            amount_needed_after_inventory = r['amount'] - inventory[r['chem']]
            n_batches = ceil(amount_needed_after_inventory / amount_out)

            for reactant in formulas[formula]:
                reactant_amount, reactant_chem = splitstr(reactant)
                reactions.put({"chem":reactant_chem, "amount": reactant_amount * n_batches})   

            leftover = (n_batches * amount_out) - amount_needed_after_inventory
            inventory[r['chem']] = leftover

    return ore_needed


## PART 1
ore_needed = eval("FUEL", 1)
print(ore_needed)

## PART 2
one_trillion = 1000000000000
amt = one_trillion // ore_needed

while(eval("FUEL", amt) <= one_trillion):
    amt += 1000

while(eval("FUEL", amt) >= one_trillion):
    amt -= 1
print(amt)