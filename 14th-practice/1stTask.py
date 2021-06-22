def pushBack(item):
    if(len(s1) == 0):
        s1.append([item, item])
    else:
        maximum = s1[len(s1)-1][1]
        
        if(item > maximum):
            maximum = item
            s1.append([item, maximum])
        else:
            s1.append([item, maximum])

def popFront():
    if(len(s2) == 0 and len(s1) != 0):
        for i in range(len(s1)):
            s2.append(s1[len(s1) - 1 - i])
        s1.clear()
        buf = s2.pop()[0]
        return buf
    elif(len(s2) != 0):
        buf = s2.pop()[0]
        return buf
    else:
        return "Error"

def max():
    if(len(s2) == 0 and len(s1) != 0):
        for i in range(len(s1)):
            s2.append([s1[len(s1) - 1 - i][0], s1[len(s1) - 1][1]])
        s1.clear()
        return s2[len(s2) - 1][1]
    elif(len(s1) != 0 and len(s2) != 0):
        maximum = s2[len(s2) - 1][1]
        
        if(maximum > s1[len(s1) - 1][1]):
            s1[len(s1) - 1][1] = maximum

        for i in range(len(s1)):
            s2.append([s1[len(s1) - 1 - i][0], s1[len(s1) - 1][1]])
        s1.clear()
        return s2[len(s2) - 1][1]
    elif(len(s1) == 0 and len(s2) != 0):
        return s2[len(s2) - 1][1]
    else:
        return "Error"


try:
    n = int(input())
except ValueError:
    print("Error")
else:
    s1, s2 = [], []

    for i in range(n):
        string = input().split(" ")
        if(string[0] == "pushBack"):
            pushBack(int(string[1]))
        elif(string[0] == "popFront" and i != 0):
            print(popFront())
        elif(string[0] == "max" and i != 0):
            print(max())
        else:
            print("Error")
