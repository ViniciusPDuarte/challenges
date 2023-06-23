print("1 = Portugues\n2 = English")
language = input("Escolha um idioma entre ingles e portugues/Choose a language between english an portuguese: ")

if language == 1:
    print("1 = subtracao")
    print("2 = soma")
    print("3 = multiplicacao")
    print("4 = divisao")
    escolha = int(input("Escolha um comando: "))

    while True:
        if escolha == 1:
            numero1 = float(input("Escolha um numero para subtrair: "))
            numero2 = float(input(f"Escolha um numero para subtrair {numero1} por: "))
            if numero1 or numero2 == 0:
                print("Erro. Conta impossivel.")
                break
            resultado = numero1 - numero2
            print("{} - {} = {}".format(numero1, numero2, resultado))
        if escolha == 2:
            numero1 = float(input("Escolha um numero para somar: "))
            numero2 = float(input(f"Escolha um numero para somar {numero1} por: "))
            if numero1 or numero2 == 0:
                print("Erro. Conta impossivel.")
                break
            resultado = numero1 + numero2
            print("{} + {} = {}".format(numero1, numero2, resultado))
        if escolha == 3:
            numero1 = float(input("Escolha um numero para multiplicar: "))
            numero2 = float(input(f"Escolha um numero para multiplicar {numero1} por: "))
            if numero1 or numero2 == 0:
                print("Erro. Conta impossivel.")
                break
            resultado = numero1 * numero2
            print("{} x {} = {}".format(numero1, numero2, resultado))
        if escolha == 4:
            numero1 = float(input("Escolha um numero para dividir: "))
            numero2 = float(input(f"Escolha um numero para dividir {numero1} por: "))
            if numero1 or numero2 == 0:
                print("Erro. Conta impossivel.")
                break
            resultado = numero1 / numero2
            print("{} : {} = {}".format(numero1, numero2, resultado))
        else:
            print("Erro. Escolha indefinida.")
            break

if language == 2:
    print("1 = subtraction")
    print("2 = addition")
    print("3 = multiplication")
    print("4 = division")
    option = int(input("Choose a command: "))

    while True:
        if option == 1:
            number1 = float(input("Choose a number to subtract: "))
            number2 = float(input(f"Choose a number to subtract {number1} by: "))
            if number1 or number2 == 0:
                print("Error. Calculation's impossible.")
                break
            result = number1 - number2
            print("{} - {} = {}".format(number1, number2, result))

        if option == 2:
            number1 = float(input("Choose a number to add: "))
            number2 = float(input(f"Choose a number to add {number1} by: "))
            if number1 or number2 == 0:
                print("Error. Calculation's impossible.")
                break
            result = number1 + number2
            print("{} + {} = {}".format(number1, number2, result))

        if option == 3:
            number1 = float(input("Choose a number to multiplicate: "))
            number2 = float(input(f"Choose a number to multiplicate {number1} by: "))
            if number1 or number2 == 0:
                print("Error. Calculation's impossible.")
                break
            result = number1 * number2
            print("{} x {} = {}".format(number1, number2, result))

        if option == 4:
            number1 = float(input("Choose a number to divide: "))
            number2 = float(input(f"Choose a number to divide {number1} by: "))
            if number1 or number2 == 0:
                print("Error. Calculation's impossible.")
                break
            result = number1 / number2
            print("{} / {} = {}".format(number1, number2, result))

        else:
            print("Erro. Escolha indefinida.")
            break
