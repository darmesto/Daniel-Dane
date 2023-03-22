# Lab 6
# Author: Dane Dickerson
# Adding code: Daniel Armesto
def encode(password):
    password_encoded = []
    for letter in password:
        new_letter = str((int(letter)+3)%10)
        password_encoded.append(new_letter)
        
    password_encoded = ''.join(password_encoded)
    return password_encoded


if __name__ == '__main__':
    while True:
        print('Menu')
        print('-'*13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter a password to encode: ')
            password_encoded = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == '2':
            print(f'The encoded password is {password_encoded}, and the original password is {password}.\n')
        elif option == '3':
            break
           
