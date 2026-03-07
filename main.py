print("-"*5,"Expense Tracker","-"*5)
expences=[]
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")
    option=int(input("Choose Option: "))
    print("-"*20)
    
    if option==1:
        catagory=input("Enter category: ")
        amount=int(input("Enter amount: "))
        date=input("Enter date: ")
        expences.append({"Catagory":catagory,"Amount":amount,"Date":date})
        print("Expense added successfully!")
        print("-"*20)
    elif option==2:
        for el in expences:
            for key,value in el.items():
                print(f"{key}:{value}")
            print("-"*20)
    elif option==3:
        pass
    elif option==4:
        print("Program exited successfully!")
        break
    else:
        print("Enter correct option.")