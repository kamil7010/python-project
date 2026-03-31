import random 
ran = random.randint(1,50)
gamecount = 0

while True:
    
    user = int(input('Enter your number your between 1-50: '))
    gamecount +=1

    if user > ran:
        print('Greater')
    elif user < ran:
        print('Lower')
    elif user == ran:
        print('You won')
        print(f'{gamecount}')
    else:
        print('Invalid number')