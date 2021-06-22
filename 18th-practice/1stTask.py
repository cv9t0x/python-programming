n, ribs = int(input()), []

for i in range(n):
    inputList = list(map(int, input().split(" ")))

    for j in range(len(inputList)):
        if inputList[j] == 1:
            listBuffer, flag = sorted([i + 1, j + 1]), False

            for k in ribs:
                if listBuffer == k:
                    flag = True
                    break

            if not flag:
                ribs.append(listBuffer)

for i in ribs:
    for j in i:
        print(j, end=" ")

    print()
