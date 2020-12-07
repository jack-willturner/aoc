formulas      = {}
with open('inputs/14', 'r') as f:
    for line in f:
        lhs, rhs = line.split('contains')[0].strip(), line.split('=>')[1].strip()
        formulas[rhs] = lhs.split(',')