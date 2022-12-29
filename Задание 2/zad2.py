if __name__ == "__main__":

    doc = input("Введите имя файла с разрешением: ")

    fileptr = open(doc, "r", encoding="utf-8")
    sentences = fileptr.readlines()

    if not fileptr.seekable():
        print("Файл с таким именем не может быть открыт или не существует")
        exit()

    k = [0, 0]
    e = 0

    for i, sentence in enumerate(sentences, 1):

        if "#" in sentence:
            k = [i, 1]
            continue
        if "def " in sentence:
            if (k[1] == 0) and (k[0] != i - 1):
                e = 1
                strname = sentence[4:len(sentence) - 1]
                print("Отсутствует комментарий (название функции, имя файла, номер строки): ", strname, doc, i)
            else:
                k[1] = 0

    if e == 0:
        print("В исходном коде нет фунций")

    fileptr.close()
