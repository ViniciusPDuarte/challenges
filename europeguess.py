# lower - portugal
# upper - PORTUGAL
# title - Portugal

print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))

if idioma == 1:
    lista = ["Portugal", "Austria", "Bielorrussia", "Dinamarca", "Belgica", "Kosovo", "Moldavia"]
    opc = input("Escolha um pais da Europa: ")

    if opc.title() in lista:
        print("=-" * 20)
        print("Parabens! Voce ganhou!")
    else:
        print("=-" * 20)
        print("Tente novamente. ")

if idioma == 2:
    list = ["Portugal", "Belgium", "Czech Republic", "Finland", "Bosnia", "Kosovo", "Croatia"]
    option = input("Guess any european country: ")

    if option.title() in list:
        print("=-" * 20)
        print("Congratulations! You won!")
    else:
        print("=-" * 20)
        print("Try Again. ")
