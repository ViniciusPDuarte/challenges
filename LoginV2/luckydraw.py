def luckyport():
    from random import randint
    from time import sleep

    py = randint(1, 49+1)
    escolha = int(input("Escolha um numero de 1 a 50 e teste a sua sorte!\nInput:"))
    sleep(0.5)
    print("=-" * 20)
    sleep(0.5)
    tent = 0
    while True:
        tent += 1
        if tent == 3:
            print("Ja se foram as tentativas!")
            sleep(0.5)
            print("Foi uma boa rodada.")
            print(f"O numero era {py}.")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            break
        if escolha == py:
            print("Nossa senhora! Tu acertaste o numero!\nBem, pelo menos es sortudo...")

        if escolha != py:
            print(f"Bem, quem esperava em acertares o numero... mais tentativas!")

        escolha = int(input("Input:"))
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)


def luckying():
    from random import randint
    from time import sleep

    py = randint(1, 49+1)
    escolha = int(input("Choose a number between 1 and 50 and test your luck!\nInput:"))
    sleep(0.5)
    print("=-" * 20)
    sleep(0.5)
    tent = 0
    while True:
        tent += 1
        if tent == 3:
            print("You used all of the attempts!")
            sleep(0.5)
            print("It was a good round.")
            print(f"The number was {py}.")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            break
        if escolha == py:
            print("Oh my god!\nWell, at least you're lucky...")

        if escolha != py:
            print(f"Uh, who was expecting you to guess it anyways... try again!")

        escolha = int(input("Input:"))
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)
