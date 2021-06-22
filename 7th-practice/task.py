with open("data/file.txt") as my_f:
    dictionary_speech = {}
    character_speech = []
    while my_f.readable() != "":
        string = my_f.readline()[:-1]
        if string == "roles:":
            while string != "textLines:":
                string = my_f.readline()[:-1]
                if string == "textLines:":
                    break
                dictionary_speech.update({string:{}})
            counter = 1
            while string != "":
                string = my_f.readline()[:-1]
                if string == "":
                    break
                i = 0
                character = ""
                speech = ""
                while string[i] != ":":
                    character += string[i]
                    i += 1
                for j in range(i + 2, len(string), 1):
                    speech += string[j]
                dictionary_speech[character].update({str(counter):speech})
                counter += 1
        if string == "":
            break
for i in dictionary_speech:
    print(i)
    for j in dictionary_speech[i]:
        print(j + ")" + dictionary_speech[i][j])
    print()