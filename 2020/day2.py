list = []
with open('inputs/day2','r') as f:
    for line in f:
        list.append(line)

def occurences(letter, string):
    count = 0
    for char in string:
        if char == letter:
            count += 1

    return count

def is_valid(line):
    conds, password = line.split(': ')
    range, letter = conds.split(' ')
    min, max = [int(i) for i in range.split('-')]

    occs = occurences(letter, password)

    if occs >= min and occs <= max:
        return True
    else:
        return False

def is_valid_b(line):
    conds, password = line.split(': ')
    range, letter = conds.split(' ')
    pos_1, pos_2 = [int(i) for i in range.split('-')]

    valid = 0
    for pos in [pos_1, pos_2]:
        if password[pos-1] == letter:
            valid += 1

    return valid == 1

valid_count = 0
for line in list:
    #print(f"{line} {is_valid_b(line)}" )
    if is_valid_b(line):
        valid_count += 1

print(valid_count)
