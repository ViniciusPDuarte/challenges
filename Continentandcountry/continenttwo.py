lista_pais = ["Chile", "Zimbabwe", "Montenegro", "Laos", "Australia"]
print("Digite tudo sem acentos.")
opc = input("Escolha um pais qualquer: ")

while True:
    if opc.title() in lista_pais:
        print("Você acertou o pais!")
    if opc.title() not in lista_pais:
        print("Não esta na base de dados.")
        if opc.title() == lista_pais[0]:
            print("Este pais é da America.")
            break
        elif opc.title() == lista_pais[1]:
            print("Este pais é da Africa.")
            break
        elif opc.title() == lista_pais[2]:
            print("Este pais é da Europa.")
            break
        elif opc.title() == lista_pais[3]:
            print("Este pais é da Asia.")
            break
        elif opc.title() == lista_pais[4]:
            print("Este pais é da Oceania.")
            break
