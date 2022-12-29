if __name__ == "__main__":
    fileptr = open("text.txt", "r", encoding="utf-8")
    sentences = fileptr.readlines()

    for sentence in sentences:
        if "?" in sentence:
            print(sentence, end='')

    for sentence in sentences:
        if "!" in sentence:
            print(sentence, end='')
