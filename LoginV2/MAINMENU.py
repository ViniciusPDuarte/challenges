from time import sleep
import languagesboth

print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))
sleep(0.5)
print("=-"*20)
sleep(0.5)

if idioma == 1:
    languagesboth.port()

if idioma == 2:
    languagesboth.ing()
