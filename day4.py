def increasing(n):
    return n[0] <= n[1] <= n[2] <= n[3] <= n[4] <= n[5]

def adjacency(n):
    poss = ['00','11','22','33','44','55','66','77','88','99']
    for p in poss:
        if p in n:
            ind = n.index(p)
            if n[ind-1] != p[0] and (not(len(n) > ind+2) or n[ind+2] != p[0]):
                return True

counter = 0
for n in range(245182,790572):
    if increasing(str(n)) and adjacency(str(n)):
        counter += 1

print(counter)

n = str(112233)
print(adjacency(n) and increasing(n))
