# This piece of code will encrypt and decrypt messages using a simple cipher like Caesar Cipher or more advanced algos like AES. This will focus on user input, error handling and clear output.
# Skills practiced will be cryptography concepts, string manipulation, and file I/O

import cryptography as crypt

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
# Store this key somewhere safe :) 
print(f"This is your key: {key}")

user_messagetoencrypt = input("Enter your Message to Encrypt Here")

token = crypt.encrypt(user_messagetoencrypt)

print("This is your encrypted data:")
print(token) 


originaldata = f.decrypt(token)

print("This is the original data:")
print(originaldata)
