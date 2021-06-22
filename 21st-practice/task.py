import sys


def searchMin(graph, checkedVertexes, checkedEdges):
    minEdge, minVertex = sys.maxsize, 0

    for i in checkedVertexes:
        for j in graph[i]:
            if (j > 0) and (graph[i].index(j) not in checkedVertexes) and (j < minEdge):
                minEdge = j
                minVertex = (i, graph[i].index(minEdge))

    checkedVertexes += [minVertex[1]]
    checkedEdges += [minVertex]


def algorithm(graph, n):
    checkedVertexes, checkedEdges = [], []
    checkedVertexes += [0]

    while len(checkedVertexes) < n:
        searchMin(graph, checkedVertexes, checkedEdges)

    return checkedEdges


def main():
    n, graph = int(input()), []

    for i in range(n):
        graph.append(list(map(int, input().split())))

    result = algorithm(graph, n)

    for i in result:
        print(i[0] + 1, ' - ', i[1] + 1)


if __name__ == "__main__":
    main()
