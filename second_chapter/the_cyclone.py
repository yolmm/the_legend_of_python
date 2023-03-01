height = int(input('How tall are you? In centimeters, please: '))
credits = int(input('How much credits do you have to ride? '))

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137:
    print('You are not tall enough to ride.')
    with_taller_person = input("Are you in company of a taller person?: ").capitalize()
    if height < 100 or with_taller_person == 'No':
        print("You can't ride.")
    elif height >= 100 and with_taller_person == 'Yes':
        print("Have fun!")
elif credits < 137:
    print("You don't have enough credits to ride.")
else:
    print("Invalid data.")