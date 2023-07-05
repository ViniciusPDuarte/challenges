import math


def calcpt():
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


def calcing():
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


def vlctypt():
    from time import sleep
    pi = math.pi
    print("vamos calcular a velocidade de um carro..")
    sleep(0.3)
    print("1. velocidade media")
    print("2. velocidade media se a aceleraçao for constante")
    print("3. velocidade circular")
    print("4. velocidade final")
    sleep(0.3)
    option = int(input("selecione um input: "))
    print("aviso: tudo esta em segundos e metros..")

    # vc == velocidade; -cal == --calculos

    if option == 1:
        initial_position = float(input("qual e a posiçao inicial? "))
        final_position = float(input("qual e a posiçao final? "))
        p_cal = initial_position - final_position
        initial_time = float(input("qual e o tempo inicial? "))
        final_time = float(input("qual e o tempo final do carro? "))
        t_cal = initial_time - final_time
        one_vc = p_cal / t_cal
        print(" (ip - fp) / (it - ft) == velocidade media de {}m/s.".format(one_vc))
        sleep(3)

    if option == 2:
        initial_velocity = float(input("qual e a velocidade inicial? "))
        final_velocity = float(input("qual e a velocidade final? "))
        two_vc = (initial_velocity + final_velocity) / 2
        print(" iv + fv / 2 == velocidade media de {}m/s.".format(two_vc))
        sleep(3)

    if option == 3:
        circle_radius = float(input("qual e o radio do circulo? "))
        time_period = float(input("qual e o periodo de tempo? "))
        twopi = (2 * pi) * circle_radius
        three_vc = twopi / time_period
        print(" ((pi x 2) * r == {}) / tempo == velocidade media de {}m/s.".format(twopi, three_vc))
        sleep(3)

    if option == 4:
        initial_velocity = float(input("qual e a velocidade inicial? "))
        acceleration = float(input("qual e a aceleraçao do carro? "))
        acceleration_time = float(input("qual e a duraçao da aceleraçao do carro? "))
        at_cal = acceleration * acceleration_time
        four_vc = at_cal + initial_velocity
        print(" (a * t == {}) == at + iv == velocidade final de {}m/s.".format(at_cal, four_vc))
        sleep(3)


def vlctying():
    from time import sleep
    pi = math.pi
    print("lets calculate a cars velocity.")
    sleep(0.3)
    print("1. Average velocity")
    print("2. Average velocity if acceleration is constant")
    print("3. Circular velocity")
    print("4. Final velocity")
    sleep(0.3)
    option = int(input("pick an input: "))
    print("warning: everything is on seconds and meters.")

    # vc == velocity; -cal == --calculation

    if option == 1:
        initial_position = float(input("whats the cars initial position? "))
        final_position = float(input("whats the cars final position? "))
        p_cal = initial_position - final_position
        initial_time = float(input("whats the cars initial time? "))
        final_time = float(input("whats the cars final time? "))
        t_cal = initial_time - final_time
        one_vc = p_cal / t_cal
        print(" (ip - fp) / (it - ft) == average velocity of {}m/s.".format(one_vc))
        sleep(3)

    if option == 2:
        initial_velocity = float(input("whats the cars initial velocity? "))
        final_velocity = float(input("whats the cars final velocity? "))
        two_vc = (initial_velocity + final_velocity) / 2
        print(" iv + fv / 2 == average velocity of {}m/s.".format(two_vc))
        sleep(3)

    if option == 3:
        circle_radius = float(input("whats the circle radius? "))
        time_period = float(input("whats the time period? "))
        twopi = (2 * pi) * circle_radius
        three_vc = twopi / time_period
        print(" ((pi x 2) * r == {}) / time == average velocity of {}m/s.".format(twopi, three_vc))
        sleep(3)

    if option == 4:
        initial_velocity = float(input("whats the cars initial velocity? "))
        acceleration = float(input("whats the cars acceleration rate? "))
        acceleration_time = float(input("whats the cars acceleration duration? "))
        at_cal = acceleration * acceleration_time
        four_vc = at_cal + initial_velocity
        print(" (a * t == {}) == at + iv == final velocity of {}m/s.".format(at_cal, four_vc))
        sleep(3)
