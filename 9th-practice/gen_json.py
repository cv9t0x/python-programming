import json

def gen_users():
    login = input("Введите логин user'a: ")
    sessionLast = input("Введите время последнего входа user'a: ")
    sessionTime = input("Введите время длительности пребывания user'a: ")

    user = {
        'login': login,
        'sessionLast': sessionLast,
        'sessionTime': sessionTime
    }

    return user

def fillInfo():
    users = []

    while(True):
        users.append(gen_users())

        check = input("\nЧтобы продолжить ввод нажмите Enter, в противном случае введите 0: ")

        if(check == "0"):
            return users

def write_json(users_dict):
    try:
        data = json.load(open('users.json'))
    except:
        data = {}
    
    data = {
        'users': users_dict
    } 

    with open('users.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def read_json():
    try:
        data = json.load(open('users.json'))
    except:
        print("Нет информации")
    
    data = json.load(open('users.json'))

    for i in range (0, len(data['users'])):
        print("Логин пользователя: " + data['users'][i]['login'] + "\n"
                + "Время последнего входа: " + data['users'][i]['sessionLast'] + "\n"
                + "Длительность пребывания на сайте: " + data['users'][i]['sessionTime'] + "\n")

def main():
    write_json(fillInfo())
    print("")
    read_json()

if __name__ == '__main__':
    main()