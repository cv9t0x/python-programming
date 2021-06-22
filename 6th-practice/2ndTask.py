n = int(input())
dict = {}
print("Введите кандидата и количество голосов за него через пробел: ")

for i in range(n):
    name, amount = input().split()
    voice = int(dict.get(name, amount))

    if voice == int(amount):
        dict.update({name:int(amount)})
    else:
        dict.update({name:int(amount) + voice})

people = sorted(dict.keys())
for i in people:
    print(i + " : " + str(dict[i]))