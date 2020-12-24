from collections import deque

cup_label = '418976235'
#cup_label = '389125467'
circle = deque()

for number in cup_label:
    circle.append(int(number))
move = 0
min_cup = min(circle)
max_cup = max(circle)



# Part 2
circle = deque()
initial_array = []
for number in cup_label:
    initial_array += [int(number)]


lookup_table = {}
for x in range(len(initial_array) - 1):
    start_number = initial_array[x]
    next_number = initial_array[x + 1]
    lookup_table[start_number] = next_number
# REMOVE BEFORE FLIGHT
lookup_table[initial_array[-1]] = initial_array[0]
    
#for x in range(end_number + 1, 1000000+1):
#    if x == end_number + 1:
#        lookup_table[initial_array[-1]] = x
 #   else:
 #       lookup_table[x - 1] = x
#lookup_table[1000000] = initial_array[0]
start_number = initial_array[0]
for x in range(100):
    first_pick = lookup_table[start_number]
    second_pick = lookup_table[first_pick]
    third_pick = lookup_table[second_pick]
    fourth_pick = lookup_table[third_pick]
    lookup_table[start_number] = fourth_pick
    destination_cup = start_number - 1
    if destination_cup < min_cup:
        destination_cup = max_cup
    while destination_cup in [first_pick, second_pick, third_pick]:
        destination_cup -= 1
        if destination_cup < min_cup:
            destination_cup = max_cup
    new_end_destination = lookup_table[destination_cup]
    lookup_table[destination_cup] = first_pick
    lookup_table[third_pick] = new_end_destination
    start_number = fourth_pick
    print('Round ' + str(x + 1))

digit = lookup_table[1]
end_label = ''
while True:
    end_label += str(digit)
    digit = lookup_table[digit]
    if digit == 1:
        break

print('Part 1:')
print('The cup label ends up ' + end_label)  


initial_array = []
for number in cup_label:
    initial_array += [int(number)]
end_number = max_cup
size_of_array = 1000000 - end_number + 1
new_array = [0] * size_of_array
full_array = initial_array + new_array
circle = deque(full_array)
lookup_table = {}
for x in range(len(initial_array) - 1):
    start_number = initial_array[x]
    next_number = initial_array[x + 1]
    lookup_table[start_number] = next_number
for x in range(end_number + 1, 1000000+1):
    if x == end_number + 1:
        lookup_table[initial_array[-1]] = x
    else:
        lookup_table[x - 1] = x
lookup_table[1000000] = initial_array[0]

check_9 = lookup_table[initial_array[-1]]
check_10 = lookup_table[check_9]
check_million = lookup_table[1000000]
start_number = initial_array[0]
for x in range(10000000):
    first_pick = lookup_table[start_number]
    second_pick = lookup_table[first_pick]
    third_pick = lookup_table[second_pick]
    fourth_pick = lookup_table[third_pick]
    lookup_table[start_number] = fourth_pick
    destination_cup = start_number - 1
    if destination_cup < min_cup:
        destination_cup = 1000000
    while destination_cup in [first_pick, second_pick, third_pick]:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = 1000000
    new_end_destination = lookup_table[destination_cup]
    lookup_table[destination_cup] = first_pick
    lookup_table[third_pick] = new_end_destination
    start_number = fourth_pick
    #print('Round ' + str(x + 1))
first_after_one = lookup_table[1]
second_after_one = lookup_table[first_after_one]
print('Part 2:')
print('Multiplying ' + str(first_after_one) + ' and ' + str(second_after_one) + ' = ' + str(first_after_one * second_after_one))
# 544297103367 too low
