f = open('aoc05.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

def listifyString(string):
    myList = []
    myList[:0] = string
    return myList

def determinePosition(qualifiers, myMin, myMax):
    half = ((myMax - myMin) + 1) / 2
    qualifier = qualifiers.pop(0)
    if (qualifier == 'F') or (qualifier == 'L'):
        if myMax - myMin == 1:
            return(myMin)
        else:
            return(determinePosition(qualifiers, myMin, myMax - half))
            
    elif (qualifier == 'R') or (qualifier == 'B'):
        if myMax - myMin == 1:
            return(myMax)
        else:
            return(determinePosition(qualifiers, myMin + half, myMax))   

seat_ID = []
for boarding_pass in problem_input:
    rowMin = 0
    rowMax = 127
    seatMin = 0
    seatMax = 7
    row = -1
    seat = -1
    nothing = False
    rows = listifyString(boarding_pass[:7])
    seats = listifyString(boarding_pass[7:])
    row = determinePosition(rows, rowMin, rowMax)
    seat = determinePosition(seats, seatMin, seatMax)
    seat_ID += [row * 8 + seat]
seat_ID.sort()

print('Part 1:')
print('Highest seat ID on a boarding pass is ' + str(max(seat_ID)))

# Part 2
# find all possible seat IDs based on mostly full flight of known seat IDs
all_seat_ID = []
for number in range(seat_ID[0],seat_ID[-1]+1):
    all_seat_ID += [number]
all_seat_ID.sort()
missing_ID = list(set(seat_ID).symmetric_difference(set(all_seat_ID)))
print('Part 2:')
print('Missing seat ID is ' + str(missing_ID[0]))
