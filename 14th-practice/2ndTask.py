n = int(input())
input_str = input().split(" ")
m = int(input())
stack= []
result = []

for i in range (n - m + 1):
    for j in range(i, i + m):
        item = int(input_str[j])
        if(len(stack) == 0):
            stack.append([item, item])
        else:
            maximum = stack[len(stack)-1][1]
            
            if(item > maximum):
                maximum = item
                stack.append([item, maximum])
            else:
                stack.append([item, maximum])
    result.append(str((stack[len(stack) - 1][1])))
    stack.clear()

print(" ".join(result))