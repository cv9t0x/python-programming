def compareWords(god, similar):
    result = 0
    buf = list(god)

    for j in range(M):
        count = 0
        for k in range(len(buf)):
            if(buf[k] in similar[j]):
                count +=1;
        if(count == len(god) - 1):
            result += 1;

    return result

gods = []
similar = []
result = []

N = int(input("Введите кол-во богов в списке: "))
print("Введите имена богов:")
for i in range(N):
    i = input()
    gods.append(i)

M = int(input("Введите кол-во похожих имен: "))
print("Введите похожие имена:")
for i in range(M):
    i = input()
    similar.append(i)

for i in range(N):
    result.append(str(compareWords(gods[i], similar)))

print("Вывод: " + " ".join(result))