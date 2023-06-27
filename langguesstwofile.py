from time import sleep
from languagelist import list_lang
while True:
    option = input("guess a language: ")
    if option.lower() in list_lang:
        print("you got it right!")
        sleep(3)
        break
    else:
        print("oops, try again.")
        sleep(1)