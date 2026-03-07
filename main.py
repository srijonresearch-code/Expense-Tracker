expences=[]
while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")
    option=int(input("Choose Option: "))

    if option==1:
        amount=int(input("Enter amount: "))
        catagory=input("Enter category: ")
        date=input("Enter date: ")
        expences.append({"Amount":amount,"Catagory":catagory,"Date":date})
    elif option==2:
        print(expences)
    elif option==4:
        print("Program exited successfully!")
        break
    else:
        print("Enter correct option: ")