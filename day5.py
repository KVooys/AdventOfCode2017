"""
Input is a set of instructions
Perform them, numbers indicate hops in the set. After every instruction, increment the current instruction by 1
"""

# Add the input as a long list
ls = []

with open('inputday5.txt', 'r') as f:
    for line in f:
        ls.append(int(line))

# print(ls)


# recursive procedure for a hop is too slow unfortunately. Will think about a better way to do this.
def hop(list, pos, steps):
    steps += 1
    # print((list, "Pos:", pos, "Current increment", list[pos], steps))

    # if number is 0, do nothing except increment the number at current pos and hop again
    if list[pos] == 0:
        list[pos] += 1
        hop(list, pos, steps)

    # not done, so we move to the correct list position and increment the number at current pos
    else:
        newpos = list[pos] + pos
        list[pos] += 1
        try:
            hop(list, newpos, steps)
        except(IndexError):
            print(list, pos, steps, "Done!")


# continuous (uglier but faster) solution instead of a recursive one
def hop2(list):
    pos = 0
    steps = 0
    while True:
        # count a new step
        steps += 1
        # print(list, pos, steps)
        # to move on, we need to move to the correct list position newpos, if possible
        if list[pos] == 0:
            list[pos] += 1
        else:
            newpos = list[pos] + pos
            list[pos] += 1
            pos = newpos
            if pos > len(list)-1:
                print(list, pos, steps)
                print("Done")
                break

# Part 2:
# if offset >3, list[pos] -=1, otherwise list[pos]+=1

def part2(list):
    pos = 0
    steps = 0
    while True:
        # count a new step
        steps += 1
        # print(list, pos, steps)
        # to move on, we need to move to the correct list position newpos, if possible
        if list[pos] == 0:
            list[pos] += 1
        else:
            newpos = list[pos] + pos
            if list[pos] >= 3:
                list[pos] -= 1
            else:
                list[pos] += 1
            pos = newpos
            if pos > len(list)-1:
                print(list, pos, steps)
                print("Done")
                break


# Start procedure at the first item in the list

#ls = [0, 3,  0,  1,  -3]
#hop(ls, 0, 0)
#hop2(ls)
part2(ls)