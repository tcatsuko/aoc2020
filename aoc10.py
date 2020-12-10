import networkx as nx
import sys
f = open('aoc10.txt','r')
problem_input = []
for line in f:
    problem_input += [int(line[:-1])]
f.close()

def find_differences(path):
    lengths = [0,0,0,0]
    for x in range(len(path)-1):
        lengths[path[x+1]-path[x]] += 1
    return lengths


adapters = [0] + problem_input
adapters += [max(adapters) + 3]
adapters.sort()
start = 0
finish = max(adapters)
G = nx.DiGraph()
for item in adapters:
    if item+1 in adapters:
        G.add_edge(item, item+1,weight=-8)
    if item+2 in adapters:
        G.add_edge(item, item+2,weight=-4)
    if item+3 in adapters:
        G.add_edge(item, item+3,weight=-2)
longest_path = nx.dijkstra_path(G, start, finish)
lengths = find_differences(longest_path)
print('Part 1:')
print('The number of 1-jolt differences multiplied by the number of 3-jolt differences is ' + str(lengths[1]*lengths[3]))

# set up a cache for counting how many ways you can be connected
cache = [0,0,1] + [0] * adapters[-1]
for a in adapters[1:]:
    i = a + 2
    cache[i] = sum(cache[i-3:i])
print('Part 2:')
print('There are ' + str(cache[-1]) + ' ways to connect the adapters together')
