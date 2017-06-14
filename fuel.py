fuel_from_user = input("How much fuel in the tank?\t")
fuel = int(fuel_from_user)
money_from_u = input("What about money?\t")
money = int(money_from_u)
if fuel > 3:
    print('It\'s OK')
    print("You ''' can drive downtown")
    if money < 10:
        print("No money... But not the problem")
    else: print("+ can drink some coffee")
else:
    print('NO fuel')
    print("Do you have money?")
    if money > 10:
        print("YES!")
        print("...We have to go to buy some fuel!")
        print('\t.......Dur-Dur-Dur-Dur. Drrrrrrrrrrrrrrrrrr')
    else:
        print("Ups. NO(")
        print("Stay at home, bomgarno)")
        print('\t.......Dur-Dur-sss...')
print("What next, buddy?")
