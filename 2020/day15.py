ls = []
with open("inputs/day15") as f:
    ls = list(map(int, f.read().split(',')))

def van_dyck_sequence(starting_list_of_ints, number_of_rounds):
    memory = {}
    for i, speak in enumerate(ls):
        memory[speak] = i+1

    speak = 0

    for i in range(len(ls)+2, 2020):
        s = f"Turn {i}: last spoken is {speak} ... "
        if memory.get(speak, None) is not None:
            new_item = (i-1) - memory[speak] 
            memory[speak] = i-1
            speak = new_item
        else:
            memory[speak] = i-1
            speak = 0

    return speak

## PART 1
print(van_dyck_sequence(ls, 2021))

## PART 2
print(van_dyck_sequence(ls, 30000001)