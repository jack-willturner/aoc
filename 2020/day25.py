
def get_loop_size(pub_key):
    val = 1
    subject_number = 7
    loop_size = 0

    while(val != pub_key):
        val *= subject_number
        val = val % 20201227
        val = int(val)
        loop_size+= 1

    return loop_size

pub_key_a = 6929599
pub_key_b = 2448427

loop_size_a = get_loop_size(pub_key_a)
loop_size_b = get_loop_size(pub_key_b)


subject_number = pub_key_a
val = 1
for loop in range(loop_size_b):
    val *= subject_number
    val = val % 20201227
    val = int(val)
print(f"{val}")

subject_number = pub_key_b
val = 1
for loop in range(loop_size_a):
    val *= subject_number
    val = val % 20201227
    val = int(val)
print(f"{val}")
