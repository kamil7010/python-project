files = 'student.csv'

def load_student():

    students = []

    try:
        with open(files , 'r') as file:
            for line in file:
                name, age, course, regno= line.strip().split(',')

                student = {
                    "name":name,
                    "age":age,
                    "course":course,
                    "regno":regno
                }
                students.append(student)

    except FileNotFoundError:
        pass

    return students

def save_student(students):

    with open(files, 'a') as file:
        for student in students:
            line = f'{student['name']}, {student['age']}, {student['course']}, {student['regno']}\n'
            file.write(line)

def add_student(students):

    name = input('Enter student name: ')
    age = input('Enter student age: ')
    course = input('Enter student course: ')
    regno = input('Enter student reg no: ')

    student = {
        "name":name, 
        "age":age,
        "course":course,
        "regno":regno
    }

    students.append(student)
    save_student(students)
    print('Saved student')

def view_student(students):

    if len(students) == 0:
         print('No found student')
    else:
        for i,std in  enumerate(students, start=1):
            print(i,std['name'],std['age'],std['course'],std['regno'])

def del_student(students):

    view_student(students)
    num = int(input('Enter number to delete: '))

    if 0 < num <= len(students):
        students.pop(num-1)
        save_student(students)
        print('student deleted')
    else:
        print('Invalid number')

def search_student(students):

    search = input('Enter search student: ')

    for student in students:
        if search in students['name'].lower():
            print(student)
        
        if search not in students['name']:
            print('no found')
               
def update_student(students):

    view_student(students)
    num = int(input('Enter number to update student: '))

    if 0 < num <= len(students):
        student = students[num-1]

        students['name'] = input()
        students['age'] = input()
        students['course'] = input()
        students['regno'] = input()
        print('student updated')

    else:
        print('Invalid number')

students = load_student()

while True:
    print('''__Student management__\n
    1. Add student\n 
    2. View student\n 
    3. Delete student\n
    4. Search student\n
    5. Update student\n
    6. Exit''')

    choice = int(input())

    if choice==1:
        add_student(students)
    elif choice==2:
        view_student(students)
    elif choice==3:
        del_student(students)
    elif choice==4:
        search_student(students)
    elif choice==5:
        update_student(students)
    elif choice==6:
        break
    else:
        print('invalid option')
print(students)