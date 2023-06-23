print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))

if idioma == 1:
    numero1 = float(input("Escolha um número qualquer, eu vou imprimir o maior: "))
    numero2 = float(input("Escolha um número qualquer: "))
    if numero1 < numero2:
        print("O número 2 é o maior dos dois.")
    if numero1 > numero2:
        print("O número 1 é o maior dos dois.")

if idioma == 2:
    number1 = float(input("Choose any number, I will print the biggest one: "))
    number2 = float(input("Choose any number: "))
    if number1 < number2:
        print("The second number's the biggest.")
    if number1 > number2:
        print("The first number's the biggest.")
