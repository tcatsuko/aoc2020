f = open('aoc25.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
door_public_key = int(problem_input[0])
card_public_key = int(problem_input[1])

door_loop_size = 0
card_loop_size = 0

# Find door loop size 
result = 1
subject_number = 7
x = 0
while result != door_public_key:
    result *= subject_number
    result = result % 20201227
    x += 1
print('Door loop size: ' + str(x))
door_loop_size = x


result = 1
subject_number = 7
x = 0
while result != card_public_key:
    result *= subject_number
    result = result % 20201227
    x += 1
print('Card loop size is ' + str(x))
card_loop_size = x

result = 1
subject_number = door_public_key
for x in range(card_loop_size):
    result *= subject_number
    result = result % 20201227

print('The encryption key is ' + str(result))