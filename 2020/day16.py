import re
from collections import OrderedDict
import numpy as np

with open("inputs/day16") as f:
    f = f.read()

f = f.split('\n\n')
f = [l.split('\n') for l in f]

conditions_list = f[0]
my_ticket       = f[1]
neighbours      = f[2]

### the conditions
conditions = OrderedDict()
i = 0
regex = '(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'
for condition in conditions_list:
    con, r1min, r1max, r2min, r2max = re.findall(regex, condition)[0]
    conditions[con] = [(int(r1min),int(r1max)),(int(r2min),int(r2max))]

## nearby tickets
val = 0

valid_rows = []

neighbours = neighbours[1:]
for i, ticket in enumerate(neighbours):
    ticket = ticket.split(',')
    ticket = [int(t) for t in ticket]


    valids = []
    for field in ticket:
        valid = any([((ranges[0][0] <= field <= ranges[0][1]) or (ranges[1][0] <= field <= ranges[1][1])) for ranges in conditions.values()])
        val += field if not valid else 0
        valids.append(valid)

    if all(valids):
        valid_rows.append(i)

## Part 1
print("Part 1: ", val)

## convert to 2D array
n = []
for r in neighbours:
    row = []
    for i in r.split(','):
        row.append(int(i))
    n.append(row)

neighbours = np.array(n)[valid_rows] # filter by valid rows

col_to_constraints = {} # map column number to the constraints it matches
for col in range(neighbours.shape[1]):
    constraints_i_match = []

    for name, constraint in conditions.items():
        rmin1, rmax1 = constraint[0]
        rmin2, rmax2 = constraint[1]

        matches_constraint = all([(rmin1 <= field <= rmax1) or (rmin2 <= field <= rmax2) for field in neighbours[:,col]])

        if matches_constraint:
            constraints_i_match.append(name)
    
    col_to_constraints[col] = constraints_i_match


    ordered_cols = sorted(col_to_constraints, key=lambda x: len(col_to_constraints[x]))

final_decisions = {}

for i, col in enumerate(ordered_cols):
    possible_cols = [c for c in col_to_constraints[col] if c not in final_decisions.values()]
    final_decisions[col] = possible_cols[0]

my_ticket = my_ticket[1:][0].split(',')
my_ticket = [int(x) for x in my_ticket]

vals = []
for k, v in final_decisions.items():
    if 'departure' in v:
        vals.append(my_ticket[k])

tot = 1
for v in vals:
    tot *= v

print(tot)