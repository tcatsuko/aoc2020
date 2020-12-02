f = open('aoc02.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
valid_passwords = 0
for line in problem_input:
    split_line = line.split()
    bounds = split_line[0].split('-')
    lower_bounds = int(bounds[0])
    upper_bounds = int(bounds[1])
    character = split_line[1][0]
    password = split_line[2]
    character_count = password.count(character)
    if character_count >= lower_bounds and character_count <= upper_bounds:
        valid_passwords += 1
print('Part 1:')
print('There are ' + str(valid_passwords) + ' valid passwords.')

# Part 2

part_2_valid_passwords = 0
for line in problem_input:
    split_line = line.split()
    bounds = split_line[0].split('-')
    lower_bounds = int(bounds[0])
    upper_bounds = int(bounds[1])
    character = split_line[1][0]
    password = split_line[2]
    if (password[lower_bounds - 1] == character) ^ (password[upper_bounds - 1]== character):
        part_2_valid_passwords += 1
print('Part 2:')
print('There are ' + str(part_2_valid_passwords) + ' valid passwords.')