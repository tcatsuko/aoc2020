f = open('aoc21.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
# Parse into ingredients and allergens
initial_ingredients = set()
allergens = set()
for line in problem_input:
    split_line = line.split(' (contains ')
    ingredients = split_line[0].split(' ')
    for ingredient in ingredients:
        initial_ingredients.add(ingredient)
    if len(split_line[1]) > 0:
        line_allergens = split_line[1][:-1].split(', ')
        for allergen in line_allergens:
            allergens.add(allergen)
# Now try to figure out what words are what allergen
decoded_ingredients = {}
allergen_ingredients = set()
for allergen in allergens:
    ingredients_lines = []
    for line in problem_input:
        if ' ' + allergen in line:
            ingredients = line.split(' (contains ')[0].split(' ')
            ingredients_lines += [set(ingredients)]
    common_ingredients = set.intersection(*ingredients_lines)
    decoded_ingredients[allergen] = list(common_ingredients)
    for item in common_ingredients:
        allergen_ingredients.add(item)
    print()
    
    
end_ingredients = initial_ingredients.copy()
for item in allergen_ingredients:
    end_ingredients.remove(item)
counted_safe = 0
for line in problem_input:
    line_set = set(line.split(' (contains ')[0].split(' '))
    counted_safe += len(line_set - allergen_ingredients)
    
print('Part 1:')
print('Counted safe ingredients ' + str(counted_safe) + ' times.')
# 2405 too high
all_found = False

while all_found == False:
    all_found = True
    for item in decoded_ingredients:
        ingredients = decoded_ingredients[item]
        if len(ingredients) > 1:
            all_found = False
            continue
        else:
            this_allergen = ingredients[0]
            for allergen in decoded_ingredients:
                if allergen == item:
                    continue
                else:
                    if this_allergen in decoded_ingredients[allergen]:
                        allergen_ingredients = decoded_ingredients[allergen]
                        allergen_ingredients.remove(this_allergen)
                        decoded_ingredients[allergen] = allergen_ingredients
allergen_list = list(allergens)
allergen_list.sort()
cdi = ''
for item in allergen_list:
    cdi += decoded_ingredients[item][0] + ','
print('Part 2:')
print('Canonical dangerious ingredient list is ' + cdi[:-1])

                    