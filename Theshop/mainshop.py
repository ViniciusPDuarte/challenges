price = 0
while True:
    # main menu
    food = [5.70, 1.10, 3.50, 8.90, 2.00]
    print('0 - Pancake, €5.70')
    print('1 - Coffe, €1.10')
    print('2 - Sandwich, €3.50')
    print('3 - Chocolate Cake, €8.90')
    print('4 - Croissant, €2.00')
    print('=-' * 30)
    option = int(input('Which food would you like? '))
    price += food[option]

    # option to pay or not
    print('=-' * 30)
    print('1 - Yes')
    print('2 - No')
    leave = int(input('Would you like to order more? '))
    print('=-' * 30)

    # conditions for payment
    if leave == 2:
        print('This is the cash machine.')
        print(f"Using your order's info, I can declare you'll need to pay {price} for your food.")
        pay = float(input('Enter the price: '))

        # calculations
        given = pay - price.__round__(2)
        need = price - pay.__round__(2)

        # return condition
        if pay > price:
            print(f'Since you paid more than needed, I will return €{given}.')
            print('=-' * 30)
            print('Bought the product with success.')
            break

        # paid less condition
        if pay < price:
            print(f'You need to pay more {need} for you to go.')
            pay = float(input('Enter the price: '))
            result = need + pay.__round__(2)
            print('=-' * 30)

        # same thing but inside, idrk why but it works
            if result > price:
                print(f'Since you paid more than needed, I will return €{given}.')
                print('=-' * 30)
                print('Bought the product with success.')
                break

            if result == price:
                print('=-' * 30)
                print('Bought the product with success.')
                break

        # normal-person payment
        if pay == price:
            print('=-' * 30)
            print('Bought the product with success.')
            break
