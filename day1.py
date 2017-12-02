"""
Day 1:
Input is a long series of numbers
Check if the number directly following the current number is the same; if so, add 1 copy of the number to the total.
Print total.
"""

# read the input and save it as string inp
inp = open('inputday1.txt', 'r').readline()
inp2 = "1221"

# main loop; check every digit against the one directly in front of it
# if they match, add them to total

def compare(inputstring):
    total = 0
    # compare the last number to the first one
    if inputstring[len(inputstring)-1] == inputstring[0]:
        total += int(inputstring[0])
    # compare all other numbers to the one in front of them
    for i in range(1, len(inputstring)):
        if inputstring[i] == inputstring[i-1]:
            total += int(inputstring[i])
    return total

def compare2(inputstring):
    # we are now not checking the number directly in front, but instead halfway across the list
    # workaround: make the series of numbers twice as long so we only need to check forward, never back
    length = len(inputstring)
    tempinp = inputstring + inputstring
    total = 0
    # compare all other numbers to the one halfway across of them
    for i in range(0, len(inputstring)):
        if tempinp[i] == tempinp[i+int(length/2)]:
            total += int(tempinp[i])
    return total



print(inp)
print(compare2(inp))