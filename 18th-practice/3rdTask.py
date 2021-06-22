n = int(input())
vertexes = [0] * n

for i in range(n):
    listBuffer = list(map(int, input().split()))

    for j in range(len(listBuffer)):
        if listBuffer[j] == 1:
            vertexes[i] += 1

for i in vertexes:
    print(i, end=" ")
