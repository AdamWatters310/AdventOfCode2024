import math

prog = list(map(int, open("input.txt").read().split(",")))


#a = 729
a = 247839539763386
b = 0
c = 0
pc = 0

def getvalue(argument):
    global a, b, c
    if argument <= 3:
        return argument
    elif argument == 4:
        return a
    elif argument == 5:
        return b
    elif argument == 6:
        return c
    else:
        print("ERROR: invalid argument")

def applyOperation(opcode, argument):
    global a, b, c, pc
    if opcode == 0:
        a = int(a//math.pow(2, getvalue(argument)))
    elif opcode == 1:
        b = int(b^argument)
    elif opcode == 2:
        b = int(getvalue(argument)%8)
    elif opcode == 3:
        if a != 0:
            pc = argument
            return False
    elif opcode == 4:
        b = int(b^c)
    elif opcode == 5:
        print(int(getvalue(argument)%8), end=",")
    elif opcode == 6:
        b = int(a//math.pow(2, getvalue(argument)))
    elif opcode == 7:
        c = int(a//math.pow(2, getvalue(argument)))
    else:
        print("ERROR: Invalid Opcode")
    return True

print("For a =", a, bin(a))

while pc < len(prog):
#    print("Running instruction", prog[pc], prog[pc+1])
    if applyOperation(prog[pc], prog[pc+1]):
        pc += 2
    