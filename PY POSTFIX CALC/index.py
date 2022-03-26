import sys   
def calculatePosfix(exp): 

    exp = exp.split()
    set = ["+", "-", "*", "/"]
    stack = []

    for i in range(0, len(exp)):
        c = exp[i]
 
        if(c.lstrip('-').isdigit()):
            stack.append(int(c))
        elif((c in set) and len(stack) >= 2):
            num1 = stack.pop()
            num2 = stack.pop()

            if(c == "+"):
                stack.append(num1 + num2)
            if(c == "-"):
                stack.append(num2 - num1)
            if(c == "*"):
                stack.append(num1 * num2)
            if(c == "/"):
                if(num1 == 0):
                    return "Zero division"
                stack.append(int(num2 / num1))
        else:
            return "Malformed expression"
    
    return stack.pop()


# print(calculatePosfix(""))
# for line in sys.stdin:
#     if(len(line) > 0):
#         print(calculatePosfix(line))

for line in sys.stdin:
    if(line.strip()):
        print(calculatePosfix(line))


# f = open(sys.argv[1], "r")
# Lines = f.readlines()
# for line in Lines:
#     if(line.strip()):
#         print(calculatePosfix(line))
