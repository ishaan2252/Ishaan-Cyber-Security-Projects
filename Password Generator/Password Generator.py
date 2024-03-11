# This is a Project to create a Random Password Generator, made by Ishaan Mehta

import secrets 



while True:
    try: 
        password_length = int(input("Input your password length requirement here as an integer"))
        if password_length <= 0: 
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive integer")

password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password = ''.join(secrets.choice(password_characters) for i in range(password_length))

print(password)