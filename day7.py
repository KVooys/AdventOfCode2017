"""
Input is a list of programs, their weight, and the programs above them
Find the lowest program in the program tree
"""
from collections import defaultdict, Counter

# used these two functions from the megathread to get a cleaner solution for part 2, thank you!

def find_weight(weights, children, node):
    # Recursively add the weight of the children to the weight of the carrying node
    return weights[node] + sum([find_weight(weights, children, child) for
                                child in children[node]])

def find_imbalance(weights, children, node):
    # If we're at a leaf node, we can't find an imbalance.
    if not children[node]: return
    child_weights = [find_weight(weights, children, child) for child in
                     children[node]]
    weight_counts = Counter(child_weights)
    # Exit early if everything is the same.
    if len(weight_counts) <= 1: return
    # The least frequent value will be the differing value.
    # N.B. Counter.most_common() returns all counts, ordered in reverse by
    # frequency. [-1] gets the last, and [0] gets the weight.
    least_frequent_weight = weight_counts.most_common()[-1][0]
    # N.B. child_weights and children[node] are in the same order.
    lfw_node = children[node][child_weights.index(least_frequent_weight)]
    # Try to find an imbalance deeper into the tree (we want to get to the leaf
    # of the problem).
    deeper_imbalance = find_imbalance(weights, children, lfw_node)
    if deeper_imbalance:
        return deeper_imbalance
    else:
        most_frequent_weight = weight_counts.most_common(1)[0][0]
        imbalance = most_frequent_weight - least_frequent_weight
        return weights[lfw_node] + imbalance


# a dict to keep track of programs, programs that have childs and the weight linked to the programs
totalprogs = set()
childprogs = defaultdict(list)
diskweight = {}

with open('inputday7.txt', 'r') as f:
    for line in f:
        currentrow = (line.split())
        # first result is the prog, 2nd is the weight, 4th and up are the child programs
        currentprog = currentrow[0]
        totalprogs.add(currentprog)
        currentweight = currentrow[1]
        diskweight[currentprog] = int(currentweight.strip('()'))
        for n in currentrow[3:]:
            child = n.replace(",", "")
            childprogs[currentprog].append(child)
            totalprogs.add(child)

    # Part 1 : Root is the only prog that is never a child.
    root = set(childprogs.keys()) - set(sum(childprogs.values(), []))
    root = root.pop()
    print(root)

    print(find_imbalance(diskweight, childprogs, root))
