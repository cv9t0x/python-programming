def heapify(arr, n, i, buf):
    min = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        min = l

    if r < n and arr[min] > arr[r]:
        min = r

    if min != i:
        buf.append([i, min])
        arr[i], arr[min] = arr[min], arr[i]
        heapify(arr, n, min, buf)


n = int(input())
inputList = input()
buf = []  # changes
heap = list(map(int, inputList.split(" ")))

for i in range(n - 1 // 2, -1, -1):
    heapify(heap, n, i, buf)

print(len(buf))

for i in buf:
    print(i)
