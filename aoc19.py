f = open('aoc19.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
x = 0
rules = {}
messages = []
x = 0
while True:
    current_line = problem_input[x]
    if current_line == '':
        x += 1
        break
    split_line = current_line.split(': ')
    current_rule = []
    if '|' in split_line[1]:
        rules_split = split_line[1].split(' | ')
        for item in rules_split:
            rule_half = []
            split_item = item.split(' ')
            rule_half += [split_item]
            current_rule += [split_item]
        rules[split_line[0]] = current_rule
    elif split_line[1] == '"a"':
        rules[split_line[0]] = 'a'
    elif split_line[1] == '"b"':
        rules[split_line[0]] = 'b'
    else:
        rule_half = []
        for item in split_line[1].split(' '):
            rule_half += [item]
        current_rule += [rule_half]
        rules[split_line[0]] = current_rule
    x += 1
print()
messages = []
for item in range(x,len(problem_input)):
    messages += [problem_input[item]]
    
def build_rule(rules, rule_list, ruleset, input_text):
    current_text = input_text
    for x in range(len(rule_list)):
        current_item = rules[rule_list[x]]
        
        if len(current_item) == 1:
            if current_item[0] == 'a':
                current_text += 'a'
                if len(rule_list) == 1:
                    ruleset.add(current_text)
            elif current_item[0] == 'b':
                current_text += 'b'
                if len(rule_list) == 1:
                    ruleset.add(current_text)
            elif len(current_item) == 1:
                build_rule(rules, current_item[0] + rule_list[x+1:], ruleset, current_text)
            else:
                for rule_number in current_item:
                    build_rule(rules, [rule_number] + rule_list[x+1:], ruleset, current_text)
        else:
            for outer_rule in current_item:
                build_rule(rules, outer_rule + rule_list[x+1:], ruleset, current_text)
    ruleset.add(current_text)
ruleset = set()
build_rule(rules, rules['0'][0], ruleset, '')



def br(rules, rule_number, ruleset, input_text):
    current_rule = rules[rule_number]

    if len(current_rule) == 1:
        for item in current_rule[0]:
            if item == 'a':
                input_text += 'a'
                ruleset.add(input_text)
            elif item == 'b':
                input_text += 'b'
                ruleset.add(input_text)
            else:
                input_text += br(rules, item, ruleset, input_text)
                
        
    else:
        for outer_rule in current_rule:
            current_text = ''
            for inner_rule in outer_rule:
                
                current_text += br(rules, inner_rule, ruleset, '')
                print()
            ruleset.add(input_text + current_text)
        input_text = current_text
    return input_text   
            

#br(rules, '0', ruleset, '')

print()
    
# Now filter the set based on max length strings
max_length = len(max(ruleset, key=len))
valid_messages = [x for x in ruleset if len(x) == max_length]

matched_messages = 0
for item in messages:
    if item in valid_messages:
        matched_messages += 1
print('Part 1:')
print('There are ' + str(matched_messages) + ' matched messages.')

    
    
