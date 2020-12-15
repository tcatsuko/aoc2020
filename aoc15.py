import datetime as dt
#spoken_numbers = [0,3,6]
#spoken_numbers = [1,3,2]
#spoken_numbers = [2,1,3]
#spoken_numbers = [2,3,1]
#spoken_numbers = [3,2,1]
#spoken_numbers = [3,1,2]
spoken_numbers = [14,8,16,0,1,17]

# Another option
seen_numbers = [0] * 2020
for x in range(len(spoken_numbers)):
    seen_numbers[spoken_numbers[x]] = x + 1
most_recent_number = spoken_numbers[-1]

#[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
#[0, 3, 6, 0, 3, 3, 1, 0, 4, 0, 2, 0, 2, 2, 1, 8, 0, 5, 0, 2]
for x in xrange(len(spoken_numbers)+1, 2020+1):
    most_recent_index = seen_numbers[most_recent_number]
    if seen_numbers[most_recent_number] > 0 and seen_numbers[most_recent_number] < x - 1:
        new_number = x - 1 - seen_numbers[most_recent_number]
        seen_numbers[most_recent_number] = x - 1
        most_recent_number = new_number
    else:
        seen_numbers[most_recent_number] = x - 1
        most_recent_number = 0
    #print(str(most_recent_number))
        
print('Part 1:')
print('The 2020th number spoken is ' + str(most_recent_number))

start_time = dt.datetime.now()
seen_numbers = [0] * 30000000
for x in range(len(spoken_numbers)):
    seen_numbers[spoken_numbers[x]] = x + 1
most_recent_number = spoken_numbers[-1]

#[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
#[0, 3, 6, 0, 3, 3, 1, 0, 4, 0, 2, 0, 2, 2, 1, 8, 0, 5, 0, 2]
for x in range(len(spoken_numbers)+1, 30000000+1):
    most_recent_index = seen_numbers[most_recent_number]
    if seen_numbers[most_recent_number] > 0 and seen_numbers[most_recent_number] < x - 1:
        new_number = x - 1 - seen_numbers[most_recent_number]
        seen_numbers[most_recent_number] = x - 1
        most_recent_number = new_number
    else:
        seen_numbers[most_recent_number] = x - 1
        most_recent_number = 0
    #print(str(most_recent_number))
end_time = dt.datetime.now()      
print('Part 2:')
print('The 30000000th number spoken is ' + str(most_recent_number))
print('This took ' + str((end_time - start_time).total_seconds()))



