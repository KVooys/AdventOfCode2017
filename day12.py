"""
Input is a bunch of numbers paired with zero or more others through a pipeline
A pipeline means bidirectional communication is possible
How big is the comm network of number 0?
"""

# define a communication storage method:
# make a dict(int:set) with every number and the set is the numbers it can communicate with.
connections = {}
with open('inputday12.txt', 'r') as f:
    for line in f:
        numbers = list(line.strip().split())
        # print(numbers)
        # we're interested in element 0, 2 and up
        currentnum = int(numbers[0])
        connectors = set()
        for n in numbers[2:]:
            connectors.add(int(n.replace(",","")))

        # create current num's connectionlist if not already there
        if currentnum not in connections.keys():
            connections[currentnum] = set()
        # add all connectors to the current num's list
        for c in connectors:
            # first create a set if not there already
            if c not in connections.keys():
                connections[c] = set()

            # add the connectors to currentnum'e sets
            connections[currentnum].add(c)
            # we also need to add the current num to all of its connectors' sets
            connections[c].add(currentnum)

# finally, after adding all normal connections, we need to add all interconnections somehow
# if a key is connected to another key, they should both include each other's values as connections

for i in connections.keys():
    for j in connections.keys():
        if j != i and j in connections[i]:
            for c1 in connections[i]:
                connections[j].add(c1)
            for c2 in connections[j]:
                connections[i].add(c2)

# print(connections[0])
# print(len(connections[0]))

# part 2: identify how many separate groups there are
# a group means all connections.values are shared
# quick fix: find the minimum numbers in all the connections.values and add them to a set, then count set length
totalgroups = set()
for s in connections.values():
    print(min(s))
    totalgroups.add(min(s))
print(totalgroups)
print(len(totalgroups))