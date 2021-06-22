import re

def check(string):
    buf = re.findall(r'[A-Z][a-z]{1,3}', string)
    if(''.join(buf) == string):
        return "YES"
    return "NO"


string = str(input("Введите руну: "))
print("Является ли строка руной: " + check(string));