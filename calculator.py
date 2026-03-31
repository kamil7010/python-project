print('Enter your number first below')
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

while True:
    
    cal1 = int(input('enter number'))
    cal2 = int(input('enter number'))
    print('\n1.add\n2.sub\n3.mul\n4.div')
    inp = input('enter which calculation to use as mentioned number')

    if inp == '1':
        print(add(cal1,cal2))
    elif inp == '2':
        print(sub(cal1,cal2))
    elif inp == '3':
        print(mul(cal1,cal2))
    elif inp == '4':
        print(div(cal1,cal2))
    else:
        print('Invalid option')

    inp2=input('Do you want recalculation Y or N').upper()

    if inp2 == "N":
        break
