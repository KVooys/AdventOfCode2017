"""

There is a pattern that spirals as follows:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

Distance = Manhattan distance (steps NEWS from square 1)
Find the distance from square 1 to square 265149
"""


# define some spiral behaviour...first steps: move until an unexplored x or y is hit, then turn left
# first coords: 0,0:1, we move x up to 1,0:2..there is nothing bigger than x1 so we turn left
# and move y up to 1,1:3 there is no bigger y, so we turn left
# and move x down to 0,1:4..there is already

# first the spiral moves 1 east, turns, 1 north, turns, 2 west, turns, 2 left, turns, etc..

def writespiral(inp):

    x = 0
    y = 0
    count = 1
    up = False
    dir = "E"
    total = 1

    for i in range(1, inp):
        print(x,y,count,dir,total)
        if dir == "E":
            x+=count
            dir = "N"
        elif dir == "W":
            x-=count
            dir = "S"
        elif dir == "N":
            y+=count
            dir = "W"
        elif dir == "S":
            y-=count
            dir = "E"
        total += count
        if up == True:
            count+=1
            up = False
        else:
            up = True
        if total > inp:
            break
    return (total)



testinp = 20
day4inp = 265149
print(writespiral(day4inp))

# last seen output = -257 -257 515 E 264711 which is 438 steps away from the goal
#, y = -257, x = -257, moving east 438 steps so final coords: 181, -257 =
# my solution does not lend itself for part 2 so I might revisit this later...