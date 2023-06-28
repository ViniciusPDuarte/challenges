print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))
letters = 0

if idioma == 1:
    word = input("Digite uma palavra, vou dizer quantas letras tem.\nTambem vou soletrar.\nInput: ")
    print("=-"*30)
    for x in word:
        print(x, end=" ")
        letters += 1

    print()
    print("=-"*30)
    print(f"A palavra tem {letters} letras.")

if idioma == 2:
    word = input("Type in a word, i will say how many letters it has.\nIll also say it letter by letter.\nInput: ")
    print("=-"*30)
    for x in word:
        print(x, end=" ")
        letters += 1

    print()
    print("=-"*30)
    print(f"It has {letters} letters.")
