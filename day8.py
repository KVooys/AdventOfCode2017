"""
Input is a set of instructions related to named registers
if the conditional is true, perform the change
Find what the largest register is at the end
"""

registers = {}

# extract variables from the instruction

test = "b inc 5 if a > 1"
highestvalue = 0

with open('inputday8.txt', 'r') as f:
    for line in f:
        (
            change_register,
            change,
            change_value,
            _if,
            check_register,
            operator,
            check_value
        ) = line.split()
        change_value, check_value = int(change_value), int(check_value)
        print(check_register, operator, check_value)

        # update registers with newly encountered dicts
        if change_register not in registers.keys():
            registers[change_register] = 0
        if check_register not in registers.keys():
            registers[check_register] = 0

        # logic on the check; different operators
        perform_operation = False

        if operator == "<" and registers[check_register] < check_value:
            perform_operation = True
        elif operator == "<=" and registers[check_register] <= check_value:
            perform_operation = True
        elif operator == ">" and registers[check_register] > check_value:
            perform_operation = True
        elif operator == ">=" and registers[check_register] >= check_value:
            perform_operation = True
        elif operator == "==" and registers[check_register] == check_value:
            perform_operation = True
        elif operator == "!=" and registers[check_register] != check_value:
            perform_operation = True

        # print(perform_operation)

        # Finally, if we have to operate, operate
        if perform_operation:
            if change == "inc":
                registers[change_register] += change_value
            if change == "dec":
                registers[change_register] -= change_value

        # part 2: keep track of highest value
        highestvalue = max(highestvalue, max(registers.values()))
print(registers)
maximum = max(registers, key=registers.get)
print(maximum, registers[maximum])
print(highestvalue)