def h(data, p=1000000007, x=263):
    buf = list(data)
    sum, i = 0, 0

    for nothing in buf:
        sum += (ord(buf[i]) * x ** int(i))
        i += 1

    return sum % p % m


def add(data):
    link = h(data)

    if (link in hTable) and (data not in hTable.values()):
        buf = data + ' ' + hTable[link]
        hTable[link] = buf
    else:
        hTable[link] = data

    return


def delete(data):
    if h(data) not in hTable.keys():
        flag = False
    else:
        if data in hTable[h(data)]:
            flag = True
        else:
            flag = False

    if flag:
        hTable[h(data)] = hTable[h(data)].replace(data, '')

    return


def find(data):
    if h(data) not in hTable.keys():
        output.append('no')
    else:
        if data in hTable[h(data)]:
            output.append('yes')
        else:
            output.append('so')

    return


def check(num):
    buf = ''

    if int(num) in hTable.keys():
        buf = hTable[int(num)]

    output.append(buf)

    return


m = int(input())
n = int(input())
output, hTable = [], {}

if (10 ** 5 < n) or (n < 1) or (n < m) or (m < n / 5):
    print('Input error')
else:
    for count in range(n):
        command = str(input()).split(' ')

        if command[0] == 'add':
            if 15 >= len(command[1]) >= 1:
                add(command[1])
            else:
                print('Length error')

        elif command[0] == 'h':
            h(command[1])

        elif command[0] == 'check':
            check(command[1])

        elif command[0] == 'del':
            delete(command[1])

        elif command[0] == 'find':
            find(command[1])

        else:
            print('Unknown command')

    print("-----------------------------------")

    for data in output:
        print(data)
