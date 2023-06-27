from random import randint
from time import sleep

print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))

if idioma == 1:
    print("a luta ira começar: ")
    print("hoje sera a luta de bruce lee vs mike tyson")
    sleep(1)

    mikeh = 100
    bruceh = 100

    while True:
        mike = randint(10, 25)
        bruce = randint(10, 25)

# mike hit
        print("=-"*30)
        if mike > 20:
            print("o mike deu um soco CRITICO de força", mike)
        else:
            print("o mike deu um soco de força", mike)
        bruceh -= mike
        print("o bruce ficou com", bruceh, "de vida.")
        sleep(0.8)

# mike comparison
        if bruceh <= 0:
            print("=-" * 30)
            print("mike ganhou a luta.")
            sleep(3)
            break

# bruce hit
        print("=-"*30)
        if mike > 20:
            print("o bruce deu um soco CRITICO de força", bruce)
        else:
            print("o bruce deu um soco de força", bruce)
        mikeh -= bruce
        print("o mike ficou com", mikeh, "de vida.")
        sleep(0.8)

# bruce comparison
        if mikeh <= 0:
            print("=-" * 30)
            print("bruce ganhou a luta.")
            sleep(3)
            break

if idioma == 2:
    print("the fight will start: ")
    print("todays fight will be bruce lee vs mike tyson")
    sleep(1)

    mikeh = 100
    bruceh = 100

    while True:
        mike = randint(10, 25)
        bruce = randint(10, 25)

        # mike hit
        print("=-" * 30)
        if mike > 20:
            print("mike hit a CRITICAL punch of strength", mike)
        else:
            print("mike hit a punch of strength", mike)
        bruceh -= mike
        print("bruce has now", bruceh, "health.")
        sleep(0.8)

        # mike comparison
        if bruceh <= 0:
            print("=-" * 30)
            print("mike won the fight.")
            sleep(3)
            break

        # bruce hit
        print("=-" * 30)
        if mike > 20:
            print("bruce hit a CRITICAL punch of strength", bruce)
        else:
            print("bruce hit a punch of strength", bruce)
        mikeh -= bruce
        print("mike has now", mikeh, "of health.")
        sleep(0.8)

        # bruce comparison
        if mikeh <= 0:
            print("=-" * 30)
            print("bruce won the fight.")
            sleep(3)
            break
