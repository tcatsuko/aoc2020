#spoken_numbers = [0,3,6]
#spoken_numbers = [1,3,2]
#spoken_numbers = [2,1,3]
#spoken_numbers = [2,3,1]
#spoken_numbers = [3,2,1]
#spoken_numbers = [3,1,2]
spoken_numbers = [14,8,16,0,1,17]
seen_numbers = {}
most_recent_number = spoken_numbers[-1]
for x in range(len(spoken_numbers)):
    seen_numbers[spoken_numbers[x]] = [x + 1]
for x in range(len(spoken_numbers)+1, 2021):
    if len(seen_numbers[most_recent_number]) > 1:
        previous_seen = seen_numbers[most_recent_number][-1]
        next_previous_seen = seen_numbers[most_recent_number][-2]
        most_recent_number = previous_seen - next_previous_seen
    else:
        most_recent_number = 0
        
    if most_recent_number in seen_numbers and len(seen_numbers[most_recent_number]) == 2:
        seen_numbers[most_recent_number][0] = seen_numbers[most_recent_number][1]
        seen_numbers[most_recent_number][1] = x
    elif most_recent_number in seen_numbers and len(seen_numbers[most_recent_number]) == 1:
        seen_numbers[most_recent_number] += [x]
    else:
        seen_numbers[most_recent_number] = [x]    
print('Part 1:')
print('The 2020th number spoken is ' + str(most_recent_number))


#spoken_numbers = [0,3,6]
#spoken_numbers = [1,3,2]
#spoken_numbers = [2,1,3]
#spoken_numbers = [2,3,1]
#spoken_numbers = [3,2,1]
#spoken_numbers = [3,1,2]
spoken_numbers = [14,8,16,0,1,17]
seen_numbers = {}
most_recent_number = spoken_numbers[-1]
for x in range(len(spoken_numbers)):
    seen_numbers[spoken_numbers[x]] = [x + 1]
for x in range(len(spoken_numbers)+1, 30000000 + 1):
    if len(seen_numbers[most_recent_number]) > 1:
        previous_seen = seen_numbers[most_recent_number][-1]
        next_previous_seen = seen_numbers[most_recent_number][-2]
        most_recent_number = previous_seen - next_previous_seen
    else:
        most_recent_number = 0
        
    if most_recent_number in seen_numbers and len(seen_numbers[most_recent_number]) == 2:
        seen_numbers[most_recent_number][0] = seen_numbers[most_recent_number][1]
        seen_numbers[most_recent_number][1] = x
    elif most_recent_number in seen_numbers and len(seen_numbers[most_recent_number]) == 1:
        seen_numbers[most_recent_number] += [x]
    else:
        seen_numbers[most_recent_number] = [x]   
        
print('Part 2:')
print('The 30000000th number spoken is ' + str(most_recent_number))


