n = int(input("Input amount of knots: "))
matrix = [[0] * n for i in range(n)]
string, list, counter = "", [], 0

while True:
    string = input("Input knots (to cancel press Enter): ")

    if string == "":
        break

    v1, v2 = map(int, string.split())

    if not list:
        list.append({v1, v2})

    for i in range(len(list)):
        if v1 in list[i]:
            list[i].add(v2)
            break

        elif v2 in list[i]:
            list[i].add(v1)
            break

        else:
            list.append({v1, v2})
            break

for i in range(len(list)):
    counter += len(list[i])

if counter == n:
    print("Min knots to repair: " + str(len(list) - 1))
else:
    print("Min knots to repair: " + str(n - counter + 1))
