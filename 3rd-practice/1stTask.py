def checkRes(item):
    if(int(item[0]) >= 1 and int(item[1]) <= 100):
        return False
    return True

def checkCode(item, width):
    if(len(str(item)) == width):
        return False    
    return True

def fillArray(w, h):
    arr = []
    for i in range(h):
        num = input("Введите код: ")
        while(checkCode(num, w)):
            num = input("Введите верный код: ")
        arr.append(num)
    return arr

def checkRul(rules):
    if(len(str(rules)) == 4):
        return False
    return True

def compareArray(arr1, arr2, rules):
    newArr = []
    rules = list(rules)
    for i in range(len(arr1)):
        buf1 = list(arr1[i])
        buf2 = list(arr2[i])
        string = ''
        for j in range(len(buf1)):
            if(buf1[j] == "0" and buf2[j] == "0"):
                string+=rules[0]
            if(buf1[j] == "0" and buf2[j] == "1"):
                string+=rules[1]
            if(buf1[j] == "1" and buf2[j] == "0"):
                string+=rules[2]
            if(buf1[j] == "1" and buf2[j] == "1"):
                string+=rules[3]
        newArr.append(string)       
    return newArr
            

res = input("Введите разрешение w на h: ").split(" ")

while(checkRes(res)):
    res = input("Введите верное разрешение w на h: ").split(" ")

w = int(res[0])
h = int(res[1])

print("Ввод данных первого изображения \n")
img1 = fillArray(w, h)
print("Ввод данных второго изображения \n")
img2 = fillArray(w, h)

rules = input("Ввод правил: ")
while(checkRul(rules)):
    rules = input("Ввод верных правил: ")

newArr = compareArray(img1, img2, rules)
print("Выходные данные: " + " ".join(newArr))