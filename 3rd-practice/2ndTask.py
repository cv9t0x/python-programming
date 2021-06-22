def checkInput(item):
    if(len(item) == n * n):
        return False
    return True

def checkSudoku(array):
    newArr = []
    check = []
    for i in range(len(array)):
        newArr += list(array[i])

    for i in range(len(array)):
        check = set(array[i])
        if(len(check) != len(array[i])):
            return False
    
    for i in range(len(newArr) - n * n):
        if(newArr[i] == newArr[i + n * n]):
            return False
    
    for m in range(n*n):
        buff = []
        for i in range(n+m, n):
            for j in range(n):
                buff += newArr[j + i*n*n];
        check = set(buff)
        if(len(check) != len(buff)):
            return False

    return True

def fillArray():
    array = [];

    for i in range(n * n):
        string = input("Введите строку судоку: ")

        while(checkInput(string)):
            string = input("Введите строку судоку заново: ")
        array.append(list(string))

    return array

n = int(input("Введи размер судоку: "))
sudoku = fillArray()

if(checkSudoku(sudoku)):
    print("Correct")
else:
    print("Incorrect")