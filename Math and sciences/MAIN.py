from time import sleep
import stage

print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))
sleep(0.5)
print("=-"*20)
sleep(0.5)

if idioma == 1:
    print("1 = matematica\n2 = ciencias")
    option1 = int(input("selecione um: "))
    if option1 == 1:
        stage.mathpt()
    if option1 == 2:
        stage.ccpt()

if idioma == 2:
    print("1 = mathandcc\n2 = sciences")
    option1 = int(input("pick one: "))
    if option1 == 1:
        stage.mathing()
    if option1 == 2:
        stage.ccing()
