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
            letter = str(int(letter) + 3)  # Convert back to string after encoding
            new_password += letter
        print("Your password has been encoded and stored!")
    elif option == 2:
        encoded_password = input('Please enter your encoded password to decode: ')

        original_password = ''
        for letter in encoded_password:
            letter = str(int(letter) - 3)  # Convert back to string after decoding
            original_password += letter
        print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
    elif option == 3:
        break