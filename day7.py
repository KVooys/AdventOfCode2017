"""
Input is a list of programs, their weight, and the programs above them
Find the lowest program in the program tree
"""
from collections import defaultdict

# a dict to keep track of programs that have childs
totalprogs = set()
childprogs = set()
diskweight = defaultdict(int)

with open('testinputday7.txt', 'r') as f:
    for line in f:
        currentrow = (line.split())
        # first result is the prog, 2nd is the weight, 4th and up are the child programs
        currentprog = currentrow[0]
        # logic to check for deepest program...if it only appears as current program and never as child, it'll be 0
        totalprogs.add(currentprog)
        currentweight = currentrow[1]
        diskweight[currentprog] = currentweight
        for n in currentrow[3:]:
            childprog = n.replace(",", "")
            childprogs.add(childprog)
            totalprogs.add(childprog)
    # print(totalprogs)
    # print(childprogs)
    print(totalprogs.difference(childprogs))
    # part 2 would need a recursive solution of some sort, will revisit later





