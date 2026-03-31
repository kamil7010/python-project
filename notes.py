import datetime

def load_notes():

    try:
        with open('notes.txt' , 'r') as file:
            return file.readlines()
        
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open('notes.txt' , 'w') as file:
        file.writelines(notes)

def add_notes(notes):
    add = input('Enter your notes: ')

    time = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

    note = f"{time} - {add}\n"

    notes.append(note)
    save_notes(notes)
    print('Note added')

def view_notes(notes):
    if len(notes) == 0:
        print('No notes found')
    else:
        print('__Your notes__')
        for i, note in enumerate(notes, start=1):
            print(i, note.strip())


def delete_notes(notes):
    view_notes(notes)
    delte = int(input('Enter note number to delete: '))

    if 0 < delte <= len(notes):
        notes.pop(delte-1)
        save_notes(notes)
        print('Note deleted')
    else:
        print('Invalid number')

def search_notes(notes):
    keyword = input('Enter keyword: ')

    for note in notes:
        if keyword in note:
            print(note.strip())

        if keyword not in note:
            print("No matching found.")

notes = load_notes()

while True:

    print('''__Notes app__\n
    1. Add notes\n 
    2. View notes\n 
    3. Delete notes\n
    4. Search notes\n
    5. Exit''')

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_notes(notes)
    elif choice == 2:
        view_notes(notes)
    elif choice == 3:
        delete_notes(notes)
    elif choice == 4:
        search_notes(notes)
    elif choice == 5:
        print('Good bye')
        break
    else:
        print("Invalid option")


print(notes)

# import datetime

# FILE_NAME = "notes.txt"

# # Function to load notes
# def load_notes():
#     try:
#         with open(FILE_NAME, "r") as file:
#             return file.readlines()
#     except FileNotFoundError:
#         return []

# # Function to save notes
# def save_notes(notes):
#     with open(FILE_NAME, "w") as file:
#         file.writelines(notes)

# # Function to add note
# def add_note(notes):
#     text = input("Enter your note: ")

#     time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     note = f"{time} - {text}\n"

#     notes.append(note)
#     save_notes(notes)

#     print("Note added!")

# # Function to view notes
# def view_notes(notes):
#     if len(notes) == 0:
#         print("No notes found.")
#     else:
#         print("\nYour Notes:")
#         for i, note in enumerate(notes, start=1):
#             print(i, note.strip())

# # Function to delete note
# def delete_note(notes):
#     view_notes(notes)

#     num = int(input("Enter note number to delete: "))

#     if 0 < num <= len(notes):
#         notes.pop(num - 1)
#         save_notes(notes)
#         print("Note deleted!")
#     else:
#         print("Invalid number")

# # Function to search notes
# def search_notes(notes):
#     keyword = input("Enter keyword: ").lower()

#     found = False

#     for note in notes:
#         if keyword in note.lower():
#             print(note.strip())
#             found = True

#     if not found:
#         print("No matching notes found.")

# # Main program
# notes = load_notes()

# while True:

#     print("\n---- NOTES APP ----")
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Delete Note")
#     print("4. Search Notes")
#     print("5. Exit")

#     choice = input("Choose option: ")

#     if choice == "1":
#         add_note(notes)

#     elif choice == "2":
#         view_notes(notes)

#     elif choice == "3":
#         delete_note(notes)

#     elif choice == "4":
#         search_notes(notes)

#     elif choice == "5":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid option")