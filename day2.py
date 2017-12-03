"""
We have an input with several rows of numbers.
We are looking for a checksum, which is the sum of the differences between the largest & smallest number in each row
"""


# part 1: transform the table to lists of ints, then return max - min
def calcsum(row):
    realrow = []
    for i in row:
        newnum = i.replace("\n", "")
        realrow.append(int(newnum))
    realrow.sort()
    print(realrow)
    return (realrow[len(realrow)-1]-realrow[0])


# part 2: instead of finding max - min, we now need to find 2 evenly divisible factors, using modulus to search for this
def calcsum2(row):
    realrow = []
    for i in row:
        newnum = i.replace("\n", "")
        realrow.append(int(newnum))
    # check for divisible factors
    for n in realrow:
        for m in realrow:
            if n%m == 0 and n!=m:
                # print(n, m, n/m)
                return (n/m)


# open input, split numbers per row and sum the checksums
with open('inputday2.txt', 'r') as f:
    total = 0
    for line in f:
        currentrow = (line.split("\t"))
        #print(currentrow)
        total += calcsum2(currentrow)
    print(total)
