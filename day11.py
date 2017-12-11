"""
Input is a set of hex movements
Find the Manhatten distance to the center hex after all movements are executed
"""

# I used cube coords to easily find max distance.
# First I define movements
def move_n(x, y, z):
    y += 1
    z -= 1
    return x, y, z

def move_nw(x, y, z):
    x -= 1
    y += 1
    return x, y, z

def move_ne(x, y, z):
    x += 1
    z -= 1
    return x, y, z

def move_s(x, y, z):
    y -= 1
    z += 1
    return x, y, z

def move_sw(x, y, z):
    x -= 1
    z += 1
    return x, y, z

def move_se(x, y, z):
    x += 1
    y -= 1
    return x, y, z


# then I run over the input file and execute the movements
with open('inputday11.txt', 'r') as f:
    movements = f.read().split(",")
    x, y, z = 0, 0, 0
    highestval = 0
    for i in movements:

        #execute movement
        if i == "n":
            x, y, z = move_n(x, y, z)
        if i == "nw":
            x, y, z = move_nw(x, y, z)
        if i == "ne":
            x, y, z = move_ne(x, y, z)
        if i == "s":
            x, y, z = move_s(x, y, z)
        if i == "sw":
            x, y, z = move_sw(x, y, z)
        if i == "se":
            x, y, z = move_se(x, y, z)

        # part 2: keep track of highest coord
        highestval = max(highestval, abs(x), abs(y), abs(z))

# total distance is the absolute value of highest coordinate
print(x, y, z)

print("Highest value:", highestval)

