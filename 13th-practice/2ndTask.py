my_stack = []
my_stack_max = [0 - sys.maxsize]

def execution(command, value):
    if command == "push":
        my_stack.append(value)
        if my_stack_max[len(my_stack_max) - 1] < value:
            my_stack_max.append(value)
        else:
            my_stack_max.append(my_stack_max[len(my_stack_max) - 1])
    elif command == "max":
        if len(my_stack) != 0:
            print(my_stack_max[len(my_stack_max) - 1])
        else:
            print("There are no values to choose from!")
    elif command == "pop":
        if len(my_stack) != 0:
            del my_stack[len(my_stack) - 1]
            del my_stack_max[len(my_stack_max) - 1]
        else:
            print("Stack is already empty!")

print("Введите количество команд:", end=" ")
n = int(input())
command_list = []
value_list = []

for i in range(n):
    string = str(input())
    if " " in string:
        command, value = string.split(" ")
        command_list.append(command)
        value_list.append(int(value))
    else:
        command_list.append(string)
        value_list.append("")
        
for i in range(len(command_list)):
    execution(command_list[i], value_list[i])