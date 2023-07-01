# noinspection PyTypeChecker
def port():
    numero1 = float(input("Escolha um número qualquer, eu vou imprimir o maior: "))
    numero2 = float(input("Escolha um número qualquer: "))
    numero3 = float(input("Escolha um número qualquer: "))
    if numero1 > numero2 and numero1 > numero3:
        print("O número 1 é o maior dos tres.")
    if numero2 > numero1 and numero2 > numero3:
        print("O número 2 é o maior dos tres.")
    if numero3 > numero2 and numero3 > numero1:
        print("O número 3 é o maior dos tres.")


def ing():
    number1 = float(input("Choose any number, I will print the biggest one: "))
    number2 = float(input("Choose any number: "))
    number3 = float(input("Choose any number: "))
    if number1 > number2 and number1 > number3:
        print("The first number's the biggest.")
    if number2 > number1 and number2 > number3:
        print("The second number's the biggest.")
    if number3 > number1 and number3 > number2:
        print("The third number's the biggest.")
