def seatnum(seatcode):
    bitmul = [64,32,16,8,4,2,1,4,2,1]
    string = [1 if c in ['B','R'] else 0 for c in seatcode]

    result = []
    for char,bit in zip(string, bitmul):
        result.append(char*bit)

    row = sum(result[:7])
    col = sum(result[7:])

    return row * 8 + col

list = []
with open('inputs/day5','r') as f:
    for line in f:
        list.append(line)

seats_taken = []
for line in list:
    seats_taken.append(seatnum(line))

## PART 1
max(seats_taken)

## PART 2
all_seats = range(min(seats_taken), max(seats_taken)+1)
print(sum(all_seats) - sum(seats_taken))
