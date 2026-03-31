contact = {}

try:

    with open('contact.txt', 'r') as file :
        for line in file:
            name , phone = line.strip().split(',')
            contact[name] = phone

except FileNotFoundError:
    contact= {}

def save_contacts():
    with open('contact.txt' , 'a') as file:
        file.write(f'{name},{phone}\n')

while True:

    print('''\n ___CONTACT BOOK___\n 
    1. Add contact\n 
    2. View contact\n 
    3. Delete contact\n
    4. Search contact\n 
    5. Exit''')

    choose = input('Choose option as mentioned above: ')

    if choose == '1':

        name = input('Enter contact name: ')
        phone = input('Enter phone number: ')
        contact[name]=phone
        save_contacts()
        print('Contact saved')

    elif choose == '2':

        if len(contact) == 0:
            print('No contact found')

        else:
            print('Your contact ')
            for name, phone in contact.items():
                print(name, '-', phone)

    elif choose == '3':

        delete = input('Enter name to delete: ')
        if delete in contact:
            delopt = input(f'Are you sure delete this {delete} contact y/n:').lower()
            if delopt == 'y':
                del contact[delete]
                save_contacts()
                print(f'{delete} contact has been deleted')

        else:
            print('Contact Not Found')

    elif choose == '4':

        search = input('Enter name to search: ')
        if search in contact:
            print(search, '-', contact[search])
        else:
            print('Contact Not Found')

    elif choose == '5':
        print('Good Bye')
        break

    else:
        print('Invalid option')

print(contact)