def mathpt():
    import mth
    print("1- matematica de velocidade")
    print("2- matematica 'normal'")
    option = int(input("qual tipo de matematica queres fazer? "))
    if option == 1:
        mth.vlctypt()
    if option == 2:
        mth.calcpt()


def mathing():
    import mth
    print("1- velocity mathandcc")
    print("2- 'normal' mathandcc")
    option = int(input("what type of mathandcc you wanna do? "))
    if option == 1:
        mth.vlctying()
    if option == 2:
        mth.calcing()


def ccing():
    import cc
    print("1- periodic table(all elements)")
    print("2- curiosities")
    option = int(input("what type of science you wanna do? "))
    if option == 1:
        print(cc.pt())
    if option == 2:
        import webbrowser
        webbrowser.open_new("https://www.nationalgeographic.com/science/")


def ccpt():
    import cc
    print("1- tabela periodica(todos os elementos)")
    print("2- curiosidades")
    option = int(input("que tipo de ciencia queres fazer? "))
    if option == 1:
        print(cc.pt())
    if option == 2:
        import webbrowser
        webbrowser.open_new("https://www.nationalgeographic.com/science/")
