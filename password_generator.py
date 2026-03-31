import random
import string

charcter = string.ascii_letters + string.digits +string.punctuation

count = int(input('How many password you want:'))
length = int(input('How many charcter you want:'))

for i in range(count):
    password = ''

    for j in range(length):
        password +=random.choice(charcter)

    print(f'password, {i+1}. {password}')