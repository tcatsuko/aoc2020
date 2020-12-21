import re

f = open('test_b_aoc19.txt','r')
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
print()

def fullmatch(regex, string, flags=0):
    """Emulate python-3.4 re.fullmatch()."""
    return re.match("(?:" + regex + r")\Z", string, flags=flags)
rule0 = rules['0']

regex = ''
for item in rule0[0]:
    regex += '(' + item + ')'
regex = '[a](([a][b])|([b][a]))'
while not bool(fullmatch('(a|b|\(|\)|\[|\]|\|)',regex)):
    print()
print()