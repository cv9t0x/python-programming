my_stack = []
string = str(input())
counter = 0
codeRed = False

for i in string:
    if i == "[" or i == "{" or i == "(":
        my_stack.append(i)
    elif i == "]":
        if my_stack[len(my_stack) - 1] == "[" and len(my_stack) != 0:
            del my_stack[len(my_stack) - 1]
        else:
            print(counter + 1)
            codeRed = True
            break
    elif i == "}":
        if my_stack[len(my_stack) - 1] == "{" and len(my_stack) != 0:
            del my_stack[len(my_stack) - 1]
        else:
            print(counter + 1)
            codeRed = True
            break
    elif i == ")":
        if my_stack[len(my_stack) - 1] == "(" and len(my_stack) != 0:
            del my_stack[len(my_stack) - 1]
        else:
            print(counter + 1)
            codeRed = True
            break
    counter += 1
    
if len(my_stack) != 0 and not codeRed:
    print(counter)
elif not codeRed:
    print("Success")