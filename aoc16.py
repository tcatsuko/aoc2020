f = open('aoc16.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
x = 0
rules = {}
my_ticket = []
tickets = []

def check_all_rules(rules, number):
    field_valid = False
    for item in rules:
        ranges = rules[item]
        for item in ranges:
            if number in item:
                field_valid = True
    return field_valid

def check_rule(ranges, field):
    in_ranges = False
    for item in ranges:
        if field in item:
            in_ranges = True
    return in_ranges

def largest_field_size(valid_fields):
    largest_size = 0
    for item in valid_fields:
        item_size = len(item)
        if item_size > largest_size:
            largest_size = item_size
    return largest_size


while True:
    current_line = problem_input[x]
    if current_line == '':
        break
    field = current_line.split(': ')[0]
    combined_ranges = current_line.split(': ')[1].split(' or ')
    rules[field] = []
    for item in combined_ranges:
        bounds = item.split('-')
        my_range = xrange(int(bounds[0]), int(bounds[1]) + 1)
        rules[field] += [my_range]
    x += 1
    
x += 1
throwaway_line = problem_input[x]
x += 1
my_ticket_string = problem_input[x].split(',')
my_ticket = []
for item in my_ticket_string:
    my_ticket += [int(item)]
x += 3
tickets = []
while x < len(problem_input):
    current_ticket_string = problem_input[x].split(',')
    current_ticket = []
    for item in current_ticket_string:
        current_ticket += [int(item)]
    tickets += [current_ticket]
    x += 1
# Parsed!

# Part 1
error_rate = 0
invalid_tickets = set()
ticket_number = 0
for ticket in tickets:
    for field in ticket:
        is_field_valid = False
        rule_check = check_all_rules(rules, field)
        if rule_check == True:
            is_field_valid = True
        #for item in rules:
        #    rule_check = check_all_rules(rules, field)
        #    if rule_check == True:
        #        is_field_valid = True
        if is_field_valid == False:
            error_rate += field
            invalid_tickets.add(ticket_number)
    ticket_number += 1
print('Part 1:')
print('Error rate is ' + str(error_rate))

# Part 2

current_ticket = 0
valid_tickets = []
for x in range(len(tickets)):
    if x not in invalid_tickets:
        valid_tickets += [tickets[x]]
valid_fields = []
for x in range(len(valid_tickets[0])):
    possibilities = []
    for field in rules:
        is_valid = True
        for ticket in valid_tickets:
            current_field = ticket[x]
            if check_rule(rules[field], current_field) == False:
                is_valid = False
        if is_valid == True:
            possibilities += [field]
    valid_fields += [possibilities]

while largest_field_size(valid_fields) > 1:
    for current_field in valid_fields:
        if len(current_field) == 1:
            for fields in valid_fields:
                if current_field == fields:
                    continue
                else:
                    if current_field[0] in fields:
                        fields.remove(current_field[0])
my_values = 1
for x in range(len(valid_fields)):
    if 'departure' in valid_fields[x][0]:
        my_values *= my_ticket[x]
print('Part 2:')
print('All departure fields multiplied is ' + str(my_values))
    
        
    