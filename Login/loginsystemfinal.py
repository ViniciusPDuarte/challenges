from getpass import getpass
from time import sleep

# language options
print("1 = Português\n2 = English")
idioma = int(input("Idioma/language: "))
sleep(0.5)
print("=-"*20)
sleep(0.5)

# portuguese
if idioma == 1:
    while True:
        print("1 - Sair do sistema;\n2 - Registrar-se.")
        escolha = int(input("Escolha uma opçao: "))
        sleep(0.5)
        print("=-"*20)
        sleep(0.5)

        if escolha == 1:
            print("Voce saiu do sistema.")
            break

        # register system
        elif escolha == 2:
            nome_usuario = input("Digite o nome do usuario: ")
            sleep(1)
            palavra_passe = getpass("Digite uma palavra-passe: ")

            if nome_usuario == palavra_passe:
                sleep(1)
                print("Erro.")
                sleep(0.5)
                print('=-' * 20)
                sleep(0.5)

            else:
                print("Registrado com sucesso.")
                sleep(0.5)
                print("=-" * 20)
                sleep(0.5)

                # login system
                while True:
                    print("1 - Sair do sistema;\n2 - Log-in;")
                    escolha = int(input("Escolha uma opçao: "))
                    sleep(0.5)
                    print("=-" * 20)
                    sleep(0.5)

                    if escolha == 1:
                        print("Voce saiu do sistema.")
                        break

                    elif escolha == 2:
                        login_usuario = input("Digite o seu usuario: ")
                        sleep(1)
                        login_passe = getpass("Digite a sua palavra-passe: ")
                        sleep(1)
                        if login_passe == palavra_passe and login_usuario == nome_usuario:
                            print("Login no sistema com sucesso.")
                            sleep(0.5)
                            print("=-" * 20)
                            break

                        else:
                            print("erro.")
                            sleep(0.5)
                            print('=-' * 20)
                            sleep(0.5)
        break

# english
if idioma == 2:
    while True:
        print("1 - Leave the system;\n2 - Register.")
        option = int(input("Choose an option: "))
        sleep(0.5)
        print("=-"*20)
        sleep(0.5)

        if option == 1:
            print("You left the system.")
            break

        # register system
        elif option == 2:
            username = input("Type your username: ")
            sleep(1)
            password = getpass("Type your password (dont worry, its going to be hidden): ")

            if username == password:
                sleep(0.5)
                print("error. try again.")
                print("=-"*20)
                sleep(0.5)

            else:
                print("Registered with success.")
                sleep(0.5)
                print("=-" * 20)
                sleep(0.5)

                # login system
                while True:
                    print("1 - Leave the system;\n2 - Log-in;")
                    option = int(input("Choose an option: "))
                    sleep(0.5)
                    print("=-" * 20)
                    sleep(0.5)

                    if option == 1:
                        print("You left the system.")
                        break

                    elif option == 2:
                        login_username = input("Type your username: ")
                        sleep(1)
                        login_password = getpass("Type your password: ")
                        sleep(1)
                        if login_password == password and login_username == username:
                            print("Login in the system with success.")
                            sleep(0.5)
                            print("=-" * 20)
                            break

                        else:
                            print("erro.")
                            sleep(0.5)
                            print('=-'*20)
                            sleep(0.5)

        break
