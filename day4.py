"""
Input is a list of passphrases separated by spaces
Check the passphrases for duplicates. If none, add +1 to the total number of correct passphrases.
Print total.
"""

def part1():
    with open('inputday4.txt', 'r') as f:
        total = 0
        for line in f:
            currentrow = (line.split(" "))
            # cut newlines first
            realrow = [i.replace("\n", "") for i in currentrow]
            # check if the amount of unique phrases is the same as the total amount of phrases
            if len(realrow) == len(set(realrow)):
                print(realrow)
                total += 1
        return total

def part2():
    with open('inputday4.txt', 'r') as f:
        total2 = 0
        for line in f:
            currentrow = (line.split(" "))
            # cut newlines first
            realrow = [i.replace("\n", "") for i in currentrow]
            # sort strings by letter
            realrow = ["".join(sorted(a)) for a in realrow]
            # check if the amount of unique phrases is the same as the total amount of phrases
            if len(realrow) == len(set(realrow)):
                print(realrow)
                total2 += 1
        print(total2)
        return total2

#part1()
part2()