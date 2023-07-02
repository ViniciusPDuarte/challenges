def rpsport():
    from random import randint
    lista = ['Pedra', 'Papel', 'Tesoura']

    print("0 = PEDRA.\n1 = PAPEL.\n2 = TESOURA")
    escolha = int(input("Escolhe um: "))
    python = randint(0, 2)

    # info
    print()
    print("=-"*20)
    print("O python escolheu", lista[python])
    print("Voce escolheu", lista[escolha])
    print("=-"*20)

    # pedra
    if escolha == 0 and python == 1:
        print("Voce perdeu.")
    elif escolha == 0 and python == 2:
        print("Voce ganhou.")
    # papel
    if escolha == 1 and python == 2:
        print("Voce perdeu.")
    elif escolha == 1 and python == 0:
        print("Voce ganhou.")
    # tesoura
    if escolha == 2 and python == 0:
        print("Voce perdeu.")
    elif escolha == 2 and python == 1:
        print("Voce ganhou.")
    # empates
    if escolha == python:
        print("Empate.")


def rpsing():
    from random import randint
    lista = ['Rock', 'Paper', 'Scissors']

    print("0 = Rock.\n1 = Paper.\n2 = Scissors")
    option = int(input("Choose one: "))
    python = randint(0, 2)

    # info
    print()
    print("=-" * 20)
    print("Python chose", lista[python])
    print("You chose", lista[option])
    print("=-" * 20)

    # rock
    if option == 0 and python == 1:
        print("You lost.")
    elif option == 0 and python == 2:
        print("You won.")
    # paper
    if option == 1 and python == 2:
        print("You lost.")
    elif option == 1 and python == 0:
        print("You won.")
    # scissors
    if option == 2 and python == 0:
        print("You lost.")
    elif option == 2 and python == 1:
        print("You won.")
    # same inputs given
    if option == python:
        print("You and python chose the same input.")
