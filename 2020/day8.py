with open('inputs/day8','r') as f:
    program = f.read()

program = program.split('\n')

def inf_loops(program, special_line=-1):
    visited = []
    lineno  = 0
    acc     = 0

    while(lineno not in visited and lineno < len(program)):
        visited.append(lineno)
        expr = program[lineno]

        if lineno == special_line:
            if "nop" in expr:
                lineno += int(expr.split(' ')[1])
            elif "jmp" in expr:
                lineno += 1
        else:
            if "nop" in expr:
                lineno += 1
            elif "acc" in expr:
                acc += int(expr.split(' ')[1])
                lineno += 1
            elif "jmp" in expr:
                lineno += int(expr.split(' ')[1])

    loops = lineno in visited
    return acc, loops

## PART 1
acc, _ = inf_loops(program)
print(acc)

## PART 2
nops = [lineno for lineno in range(len(program)) if 'nop' in program[lineno]]
jmps = [lineno for lineno in range(len(program)) if 'jmp' in program[lineno]]

for special_line in (nops+jmps):
    acc, loops = inf_loops(program, special_line)
    if not loops:
        print(acc)