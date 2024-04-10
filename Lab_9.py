#Encoder: Albert Lorie

while True:
    print('''\nMenu
-------------
1. Encode
2. Decode
3. Quit''')

    option = int(input('\nPlease enter an option: '))
    if option == 1:
        password = input('Please enter your password to encode: ')

        new_password = ''
        for letter in password:
            letter = int(letter) + 3
            new_password += f'{letter}' #stored in this list
        print("Your password has been encoded and stored!")
    elif option == 2:
        #decoder
        pass


    elif option == 3:
        break


