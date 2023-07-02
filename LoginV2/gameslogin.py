def gamesport():
    from time import sleep
    import luckydraw
    import rpsgame
    times = 0
    while True:
        print("1 - Sair do sistema;\n2 - Jogo da sorte;\n3 - Pedra papel ou tesoura.")
        escolha = int(input("Escolha uma opçao: "))
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)
        if escolha == 1:
            print("Voce saiu do sistema.")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            break

        if escolha == 2:
            luckydraw.luckyport()
        if escolha == 3:
            rpsgame.rpsport()
        if times == 2:
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            print("Obrigado por usar este programa.")
            sleep(3)
            break

        times += 1


def gamesing():
    from time import sleep
    import luckydraw
    import rpsgame
    times = 0
    while True:
        print("1 - Leave the system;\n2 - Lucky-draw;\n3 - Rock paper scissors.")
        escolha = int(input("Choose an input: "))
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)
        if escolha == 1:
            print("You left the system.")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            break

        if escolha == 2:
            luckydraw.luckying()
        if escolha == 3:
            rpsgame.rpsing()
        if times == 2:
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            print("Thanks for using this program!")
            sleep(3)
            break

        times += 1
