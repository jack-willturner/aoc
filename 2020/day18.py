import re

exprs = []

with open("inputs/day18") as f:
    for line in f:
        exprs.append(line.replace('\n',''))

def eval_expr(s):
    nums = re.findall(r"[0-9]+", s)
    ops  = re.findall(r"[\+\*]", s)
    if all([op=='+' for op in ops]) or all([op=='*' for op in ops]):
        for i, (n1, n2) in enumerate(zip(nums, nums[1:])):
            nums[i+1] = eval(f"{n1} {ops[i]} {n2}")
    else:
        s = re.sub(r"[0-9]+\+[0-9]+", lambda x: str(eval_expr(x[0])), s)
        return eval_expr(s)
    return nums[-1]

acc = 0
for s in exprs:
    s = s.replace(' ','')
    while('(' in s):
        s = re.sub(r"\([0-9]+[\+\*][0-9]+([\+\*]+[0-9]+)*\)"+
                    r"|\([0-9]+[\+\*][0-9]+[[\+\*] +[0-9]+]*\)", lambda x: str(eval_expr(x[0])) , s)
    acc += eval_expr(s)

print(acc)