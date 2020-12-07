def split_bag_expr(bag_expr):
    bag_expr = bag_expr.strip()
    num = bag_expr[0]
    colour = bag_expr[1:].split('bag')[0].strip()
    return num, colour

bags = {}

with open('inputs/day7', 'r') as f:
    for line in f:
        line = line.replace('.','')
        lhs, rhs = line.split('contain')[0].strip(), line.split('contain')[1].strip()
        colour = lhs.split('bags')[0].strip()

        if (rhs == "no other bags"):
            succs = None
        else:
            succs = {}

            successors = rhs.split(',')
            for succ in successors:
                num, col = split_bag_expr(succ)
                succs[col] = num     

        bags[colour] = succs

colours = list(bags.keys())


### PART 1
def can_hold(colour):    
    succs = bags[colour]
    if succs is None:
        return False
    elif 'shiny gold' in list(succs.keys()):
        return True
    else:
        return any([can_hold(col) for col in succs.keys()])
    
can_hold('dark orange')
valid = 0      
for col in colours:
    if not(col == 'shiny gold'):
        valid += 1 if can_hold(col) else 0

print(valid)

## PART 2
def how_many(col):
    succs = bags[col]
    if succs is None:
        return 1
    else:
        # me plus + immediate succ
        return 1 + sum([(how_many(s)*int(succs[s])) for s in succs.keys()])

print(how_many('shiny gold') - 1)