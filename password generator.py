# I import our random module
import random
import string

# password characyters
alphabets = string.ascii_lowercase
alpha = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# we define the characters
characters = alphabets + alpha + numbers + symbols

# I ask the user to input the length of characters using input
pwdlen = int(input('Enter password length: '))

# generating a password
pwd = ''
for i in range(pwdlen):
    pwd += ''.join(random.choice(characters))
print(pwd)