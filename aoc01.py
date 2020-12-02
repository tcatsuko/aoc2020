f = open('aoc01.txt','r')
problem_input = []
for line in f:
    problem_input += [int(line)]
f.close()

def find_addend(my_array, my_sum, addends):
    for number in my_array:
        other_number = my_sum - number
        if addends == 2:
            if other_number in my_array:
                return (number, other_number,-1)
        else:
            new_array = my_array[:]
            new_array.remove(number)
            (num2, num3, nothing) = find_addend(new_array, other_number, 2)
            if num2 > 0 and num3 > 0:
                return(number, num2, num3)
    
    return (-1,-1,-1)

(number, other_number,nothing) = find_addend(problem_input, 2020,2)

print('Part 1:')
print('Numbers are ' + str(number) + ' and ' + str(other_number))
part1 = number * other_number
print('Answer is ' + str(part1))

number1 = -1
number2 = -1
number3 = -1

# Now need to find 3 numbers that add up to 2020
(number1, number2, number3) = find_addend(problem_input, 2020, 3)
print('Part 2:')
print('Numbers are ' + str(number1) + '. ' + str(number2) + ', and ' + str(number3))
part2 = number1 * number2 * number3
print('Andwer is ' + str(part2))
