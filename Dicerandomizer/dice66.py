from random import randint
from time import sleep

print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))
attempts = 0

if idioma == 1:
    print("vamos ver quantas tentativas leva para 2 dados chegarem ao numero 6")
    print("=-"*30)

    while True:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        if dice1 == 6:
            if dice2 == 6:
                print("=-" * 30)
                print("1 - ({}) | 2 - ({})".format(dice1, dice2))
                print(f"demorou {attempts} tentativas para os dois chegarem ao seis.")
                sleep(3)
                break

        sleep(0.2)
        attempts += 1
        print("1 - ({}) | 2 - ({})".format(dice1, dice2))

if idioma == 2:
    print("lets see how many attempts it takes for 2 dices to  reach the number 6")
    print("=-"*30)

    while True:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        if dice1 == 6:
            if dice2 == 6:
                print("=-" * 30)
                print("1 - ({}) | 2 - ({})".format(dice1, dice2))
                print(f"it took {attempts} attempts for both to be six..")
                sleep(3)
                break

        sleep(0.2)
        attempts += 1
        print("1 - ({}) | 2 - ({})".format(dice1, dice2))
