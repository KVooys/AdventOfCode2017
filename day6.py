"""
Input is a list of banks and their current mem
A mem distribution program performs a function.
Every cycle, the program takes the largest bank and pours it over the banks, starting at the next bank.
Find when the program produces the same result as it has earlier
"""



# a list to keep track of earlier distributions
solutions = list()

ls = list()
with open('inputday6.txt', 'r') as f:
    for i in f.read().split("\t"):
        ls.append(int(i))


def redistribute(ls):
    length = len(ls)

    # the blocks to distribute, and the index to start from
    blocks = max(ls)
    curindex = ls.index(blocks)
    # remove all blocks at current position
    ls[curindex] = 0
    # start 1 position further
    curindex += 1
    # main loop. after placing every block we move 1 index to the right.
    # If not possible, continue from the left of the list again
    for i in range(blocks):
        ls[(curindex)%length] += 1
        curindex += 1
    solutions.append(ls.__str__())


# test = [0, 2, 7, 0]

# keep track of number of cycles
count = 0
while len(solutions) == len(set(solutions)):
    redistribute(ls)
    count += 1
else:
    print(solutions)
    print(count)

    # part 2: once the looping part is found, check how many times it can loop before it finds itself again
    # I did this by starting with the first recurring solution and using it in the main loop again
    newlist = ls
    print(newlist)
    solutions = list()
    solutions.append(ls.__str__())
    newcount = 0
    while len(solutions) == len(set(solutions)):
        redistribute(newlist)
        newcount += 1
    else:
        print(solutions)
        print(newcount)


