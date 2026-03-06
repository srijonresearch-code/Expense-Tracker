print("Expense Tracker")
print("1. Add Expense")
print("2. View Expenses")
print("3. View Total Spent")
print("4. Exit")
option=int(input("Choose Option: "))

if option==1:
    amount=int(input("Enter amount: "))
    catagory=(input("Enter category: "))
    date=input("Enter date: ")
    