def is_complete(arr, n):

    for i in range(int((n-2) / 2) + 1):
        l = 2 * i + 1
        r = 2 * i + 2

        if(arr[l] > arr[i]):
            return False

        if(r < n and arr[r] > arr[i]):
            return False

    return True


inputList = input()
tree = list(map(int, inputList.split()))
print("Is tree complete: " + str(is_complete(tree, len(tree))))
