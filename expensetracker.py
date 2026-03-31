expenses = []

# try:
#    with open('expenses.txt', 'r') as file:
#        expe = file.read().splitlines()

# except FileNotFoundError:
#    expenses = []

# def save_expenses():
#    with open('expenses.txt', 'w') as file:
#        for exp,amts in expenses:
#            file.write((exp,amts) , '\n')

while True:
    print('''\n ___Expenses Tracker___
    1. Add Expense\n
    2. View Expenses\n
    3. Show Total Expense\n
    4. Exit''')

    choice = input('Enter your choice as above mentioned list: ')
    if choice == '1':
        catagory = input('Enter your expenses: ')
        amt = int(input('Enter your amount: '))
        expenses.append((catagory, amt))
        # save_expenses()
        print('Your expenses added')

    elif choice == '2':
        if len(expenses)==0:
            print('No expenses found..')
        else:
            for catagory , amt in expenses:
                print(catagory, '-' , amt)

    elif choice == '3':
        total = sum(amount for catagory, amount in expenses)
        print(f'Total expenses = {total}')

    elif choice == '4':
        print('Good Bye')
        break

    else:
      print('Invalid expenses')


# expenses = []

# while True:

#     print("\n---- EXPENSE TRACKER ----")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Show Total Expense")
#     print("4. Exit")

#     choice = input("Choose option: ")

#     if choice == "1":

#         category = input("Enter expense category: ")
#         amount = float(input("Enter amount: "))

#         expenses.append((category, amount))

#         print("Expense added!")

#     elif choice == "2":

#         if len(expenses) == 0:
#             print("No expenses recorded.")

#         else:
#             print("\nYour Expenses:")

#             for category, amount in expenses:
#                 print(category, ":", amount)

#     elif choice == "3":

#         total = sum(amount for category, amount in expenses)

#         print("Total Expense =", total)

#     elif choice == "4":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid option")






