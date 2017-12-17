"""
Input is a single number: 356 in my case
Starting at 0, a spinlock will step forward 356 steps through a circular buffer,
and insert the next number after the position it lands on.
It will repeat this process 2017 times, inserting the next number every time.
Answer is the number next to 2017 after this process ends.
"""

from collections import deque


# a way to keep track of the buffer; it is basically an ordered list that becomes 1 longer every time.
startbuffer = [0]
buffer2 = deque([0])
# zero-based position of the stepping procedure
startpos = 0

teststep = 3
currentstep = 356

# another way to do it is a dict, using the position in the buffer as coordinates of some sort.

# this function will perform one step procedure + insertion
def rotate(buffer, step, pos):

    for i in range(1, 2018):

        # move through the buffer 'step' steps, making sure to loop back to the front if the end is reached
        # if the buffer is 5 long, and we move 11 steps, starting at pos 1, new pos would be (1 + 0 + 11) % 5 = 2
        pos = (1 + pos + step) % len(buffer)
        # print(pos)
        # insert the current number at the position
        buffer.insert(pos+1, i)

    print(buffer)
    print(buffer.index(2017), buffer[buffer.index(2017)+1])


# part 2:
# used a faster data type like a deque, wonder if a linked list would also work..

def rotate2(buffer, step, pos):
    for i in range(1, 50000001):
        buffer.rotate(-step)
        buffer.append(i)
    print(buffer.index(0), buffer[buffer.index(0) + 1])


# rotate(startbuffer, currentstep, startpos)
rotate2(buffer2, currentstep, startpos)