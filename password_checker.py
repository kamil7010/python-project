password = input('Enter password: ')
score = 0 

if len(password) >= 8:
    score +=1

else:
    print('Password must be at least 8 charcter')

if any(char.isupper() for char in password):
    score +=1
else:
    print('Add uppercase charctere in your password')

if any(char.islower() for char in password):
    score +=1
else:
    print('Add lower charctere in your password')

if any(char.isdigit() for char in password):
    score +=1
else:
    print('Add digit charctere in your password')

special = '!@$%&^#*'

if any(char in special for char in password):
    score +=1
else:
    print('Add special charctere in your password')

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")