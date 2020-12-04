f = open('aoc04.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

# concatenate passports into single strings
passports = []
current_passport = ''
for line in problem_input:
    if line == '':
        passports += [current_passport[:-1]]
        current_passport = ''
    else:
        current_passport += line + ' '
passports += [current_passport[:-1]]

def has_required_field_lenient(passport_array):
    input_field = passport_array.split(':')
    if input_field[0] == 'byr':
        return True
    if input_field[0] == 'eyr':
        return True
    if input_field[0] == 'hgt':
        return True
    if input_field[0] == 'hcl':
        return True
    if input_field[0] == 'ecl':
        return True
    if input_field[0] == 'iyr':
        return True
    if input_field[0] == 'pid':
        return True
    return False

def has_required_field_strict(passport_array):
    input_field = passport_array.split(':')
    if input_field[0] == 'byr':
        if len(input_field[1]) != 4:
            return False
        if int(input_field[1]) >= 1920 and int(input_field[1]) <= 2002:
            return True
        else:
            return False
    if input_field[0] == 'eyr':
        if len(input_field[1]) != 4:
            return False
        if int(input_field[1]) >= 2020 and int(input_field[1]) <= 2030:
            return True
        else:
            return False         

    if input_field[0] == 'hgt':
        if 'cm' in input_field[1]:
            raw_height = int(input_field[1].replace('cm',''))
            if raw_height >= 150 and raw_height <= 193:
                return True
        elif 'in' in input_field[1]:
            raw_height = int(input_field[1].replace('in',''))
            if raw_height >= 59 and raw_height <= 76:
                return True
        return False

    if input_field[0] == 'hcl':
        color = input_field[1]
        if color[0] != '#':
            return False
        color = color.replace('#','')
        if len(color) != 6:
            return False
        for character in color:
            if not ((character >= 'a' and character <= 'f') or (character >= '0' and character <= '9')):
                return False
        return True
    if input_field[0] == 'ecl':
        ecl = input_field[1]
        if ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
            return True
        return False
    if input_field[0] == 'iyr':
        if len(input_field[1]) != 4:
            return False
        if int(input_field[1]) >= 2010 and int(input_field[1]) <= 2020:
            return True
        else:
            return False        
 
    if input_field[0] == 'pid':
        pid = input_field[1]
        if len(pid) != 9:
            return False
        for number in pid:
            if not (number >= '0' and number <= '9'):
                return file
        return True
    return False

# part 1: count valid passports
valid_passports = 0
for passport in passports:
    valid_fields = 0
    # Split the fields
    split_fields = passport.split(' ')
    for item in split_fields:
        has_field = has_required_field_lenient(item)
        if has_field == True:
            valid_fields += 1
   
    if valid_fields >= 7:
        valid_passports += 1
print('Part 1:')
print('There are ' + str(valid_passports) + ' loosely checked valid passports in the list.')
# 263 too low

# part 2: strict checking
valid_passports = 0
for passport in passports:
    valid_fields = 0
    # Split the fields
    split_fields = passport.split(' ')
    for item in split_fields:
        has_field = has_required_field_strict(item)
        if has_field == True:
            valid_fields += 1
   
    if valid_fields >= 7:
        valid_passports += 1
print('Part 2:')
print('There are ' + str(valid_passports) + ' strictly checked valid passports in the list.')