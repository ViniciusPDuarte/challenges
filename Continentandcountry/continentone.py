lista_pais = ["Chile", "Zimbabwe", "Montenegro", "Laos", "Australia"]
lista_cont = ["America", "Africa", "Europa", "Asia", "Oceania"]
print("Digite tudo sem acentos.")
opc = input("Escolha um pais qualquer: ")

if opc.title() in lista_pais:
    print("Você acertou o pais!")
    if opc.title() == lista_pais[0]:
        cont = input("Indique de que continente ele é: ")
        if cont.title() == lista_cont[0]:
            print("Você acertou tudo! Parabens!")
    if opc.title() == lista_pais[1]:
        cont = input("Indique de que continente ele é: ")
        if cont.title() == lista_cont[1]:
            print("Você acertou tudo! Parabens!")
    if opc.title() == lista_pais[2]:
        cont = input("Indique de que continente ele é: ")
        if cont.title() == lista_cont[2]:
            print("Você acertou tudo! Parabens!")
    if opc.title() == lista_pais[3]:
        cont = input("Indique de que continente ele é: ")
        if cont.title() == lista_cont[3]:
            print("Você acertou tudo! Parabens!")
    if opc.title() == lista_pais[4]:
        cont = input("Indique de que continente ele é: ")
        if cont.title() == lista_cont[4]:
            print("Você acertou tudo! Parabens!")
