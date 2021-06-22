print("Введите количество классов:", end=" ")
n = int(input())
boysDict = {}
rateDict = {}
vs = []
counter = 0

for i in range(n):
    print("Введите количество мальчиков и девочек через пробел в " + str(i + 1) + " классе")
    boys, girls = input().split()

    if int(boys) > int(girls):
        vs.append(i)
        counter += 1

    boysDict.update({i:(int(boys) / (int(boys) + int(girls)))})
    rateDict.update({(int(boys) / (int(boys) + int(girls))):i})

boysList = sorted(boysDict.values())
print("Номера классов по возрастанию процента мальчиков: ")

for i in boysList:
    print(rateDict[i] + 1, end=" : ")
    print(i)

print("Количество классов, в которых количество мальчиков превышает количество девочек: " + str(counter))

if(counter > 0):
    print("Номера этих классов:")
    for i in vs:
        print(i + 1)
