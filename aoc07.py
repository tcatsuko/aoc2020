import networkx as nx

f = open('aoc07.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

def find_bags(g, color):
    edges = list(g.out_edges(color))
    bags = 0
    for edge in edges:
        child = edge[1]
        weight = g[color][child]['weight']
        bags += weight + (weight * find_bags(g,child))
    return bags

# Parse input
split_info = []
for line in problem_input:
    split_line = line.split(' contain ')
    split_info += [split_line]
g = nx.DiGraph()

for bag in split_info:
    parent_bag_line = bag[0]
    children_bag_line = bag[1]
    if 'no other' in children_bag_line:
        continue
    parent_bag_colors = parent_bag_line.split(' ')
    parent_bag_color = parent_bag_colors[0] + ' ' + parent_bag_colors[1]
    split_children = children_bag_line.split(', ')
    for child in split_children:
        split_child = child.split(' ')
        child_color = split_child[1] + ' ' + split_child[2]
        child_number = int(split_child[0])
        g.add_edge(parent_bag_color, child_color, weight=child_number)

edges = list(nx.edge_dfs(g, source='shiny gold', orientation='reverse'))
# Now parse the output
colors_set = set()
for edge in edges:
    colors_set.add(edge[0])
print('Part 1:')
print(str(len(colors_set)) + ' bag colors can contain at least one shiny gold bag.')
# part 2
#edges = list(g.out_edges('shiny gold'))
total_bags = find_bags(g,'shiny gold')
print('Part 2:')
print('A shiny gold bag must contain ' + str(total_bags) + ' other bags.')


    