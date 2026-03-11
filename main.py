import json
print("-"*8,"Expense Tracker","-"*8)
with open("expenses.json","r") as file:
    expense=json.load(file)
while True:
    print(f"1. Add Expense")
    print(f"2. View Expenses")
    print(f"3. View Total Spent")
    print(f"4. Delete Expense")
    print(f"5. Clear Expenses")
    print(f"6. Exit")
    option=int(input("Choose Option: "))
    print("-"*20)
    
    if option==1:
        category=input(f"Enter category: ")
        amount=int(input(f"Enter amount: "))
        date=input(f"Enter date: ")
        expense.append({"Category":category,"Amount":amount,"Date":date})
        with open("expenses.json","w") as file:
            json.dump(expense,file)
        print(f"Expense added successfully!")
        print("-"*20)
    elif option==2:
        index=0
        print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
        print("."*36)
        while index<len(expense):
            print(f"{index}. {expense[index]["Category"]:<12}{expense[index]["Amount"]:<10}{expense[index]["Date"]:<12}")
            index+=1
        print("-"*20)    
    elif option==3:
        total_spent=0
        index=0
        while index<len(expense):
            total_spent=total_spent+expense[index]["Amount"]
            index+=1
        print(f"Total spent: {total_spent}")
        print("-"*20)
    elif option==4:
        index=0
        print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
        print("."*36)
        while index<len(expense):
            print(f"{index}. {expense[index]["Category"]:<12}{expense[index]["Amount"]:<10}{expense[index]["Date"]:<12}")
            index+=1
        print("-"*20)
        delete_index=int(input("Enter number to delete: "))
        expense.pop(delete_index)
        print("Expense deleted successfully!")
        print("-"*20)
    elif option==5:
        with open("expenses.json","w") as file:
            json.dump([],file)
            expense=[]
        print(f"Expenses cleared successfully!")
        print("-"*20)    
    elif option==6:
        print(f"Program exited successfully!")
        print("-"*20)
        break
    else:
        print(f"Please enter correct option.")
        print("-"*20)