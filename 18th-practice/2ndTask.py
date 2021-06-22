vertexes, ribs = map(int, input().split())
matrix = [[0] * vertexes for i in range(vertexes)]

for i in range(ribs):
    v1, v2 = map(int, input().split())
    matrix[v1 - 1][v2 - 1] = 1
    matrix[v2 - 1][v1 - 1] = 1

for i in range(vertexes):
    for j in range(vertexes):
        print(matrix[i][j], end=" ")
    print("")
