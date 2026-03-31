tasks = []

try:
    with open('tasks.txt','r') as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks= []



def savetasks():
    with open('tasks.txt' , 'a') as file:
        for task in tasks:
             file.write(task + '\n')

while True:

    print('''\n ___TODO LIST___\n 
    1. Add task\n 
    2. View task\n 
    3.Delete task\n 
    4. Exit''')


    chioce = input()
    if chioce =='1':
        tas = input('enter youe task: ')
        tasks.append(tas)
        savetasks()
        print('Task added')

    elif chioce == '2':
        if len(tasks) == 0:
            print('No tasks found')
        else:
            for i, task in enumerate(tasks, start=1):
                print(i,".", task)   

    elif chioce == '3':
        if len(tasks) == 0:
            print('No tasks found')
        else:
            for i, task in enumerate(tasks, start=1):
                print(i,".", task)   

            remove = int(input('Enter which task to delete as menioned in list number: '))
            if remove > 0 & remove <= len(tasks):
                tasksnum = tasks[remove-1]
                confirm = input(f'Are you sure {tasksnum} remove (y/n): ')
                if confirm == 'y':
                    tasks.pop(remove-1)
                    savetasks()
                    print('Deleted successfully')
                else:
                    print('Deletion cancelled')

            else:
                print("invalid tasks")
    elif chioce=='4':
        print("GoodBye")
        break
    
    else:
        print("invalid option")


print(tasks)       