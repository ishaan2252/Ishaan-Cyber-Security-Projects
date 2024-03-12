# This piece of code will encrypt and decrypt messages using a simple cipher like Caesar Cipher or more advanced algos like AES. This will focus on user input, error handling and clear output.
# Skills practiced will be cryptography concepts, string manipulation, and file I/O

import cryptography

from cryptography.fernet import Fernet

# Generating Cryptographic Key, printing this out to the end user. Would not do this "typically", but doing this for ease of readability to user
key = Fernet.generate_key()
f = Fernet(key)
# Store this key somewhere safe :) 
print(f"This is your key, store this in a safe place: {str(key)}")

# Prompt the end user to input the string they want encrypted.
user_Message_To_Encrypt = input("Enter your Message to Encrypt Here: ")

# Encrypt the message entered using the token stored as "f"
token = f.encrypt(user_Message_To_Encrypt.encode())

# Print to user the token (encrypted data)
print("This is your encrypted data:")
print(token) 


originaldata = f.decrypt(token)

print("This is the original data:")
print(originaldata.decode())
