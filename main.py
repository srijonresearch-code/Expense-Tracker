import json
with open("expences.json","r") as file:
    expences=json.load(file)
print(expences)
print("-"*5,"Expense Tracker","-"*5)
expence=[]
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
        expence.append({"Catagory":catagory,"Amount":amount,"Date":date})
        print("Expense added successfully!")
        print("-"*20)
    elif option==2:
        for el in expence:
            for key,value in el.items():
                print(f"{key}:{value}")
            print("-"*20)
    elif option==3:
        for element in expence:
            for key,value in element.items():
                if value==amount:    
                    total_spent=0
                    for amount_value in element.items():
                        total_spent+=amount
        print("Total spent: ",total_spent)
        print("-"*20)
    elif option==4:
        print("Program exited successfully!")
        print("-"*20)
        break
    else:
        print("Enter correct option.")
        print("-"*20)