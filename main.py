import json
print("-"*8,"Expense Tracker","-"*8)
try:
    with open("expenses.json","r") as file:
        expense=json.load(file)
except:
    expense=[]        
while True:
    print(f"1. Add Expense")
    print(f"2. View Expenses")
    print(f"3. View Total Spent")
    print(f"4. View Total Expenses")
    print(f"5. Delete Expense")
    print(f"6. Clear Expenses")
    print(f"7. Exit")
    try:
        option=int(input("Choose Option: "))
    except ValueError:
        print("Invalid input :(")
        print("-"*20)
        continue
    print("-"*20)  
    if option==1:
        category=input(f"Enter category: ")
        try:
            amount=int(input(f"Enter amount: "))
        except ValueError:
            print("Invalid input :(")
            print("-"*20)
            continue
        date=input(f"Enter date: ")
        expense.append({"Category":category,"Amount":amount,"Date":date})
        with open("expenses.json","w") as file:
            json.dump(expense,file)
        print(f"Expense added successfully! ^_^")
        print("-"*20)
    elif option==2:
        index=0
        print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
        print("-"*36)
        while index<len(expense):
            print(f"{index}. {expense[index]['Category']:<12}{expense[index]['Amount']:<10}{expense[index]['Date']:<12}")
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
        print(f"Total Expenses: {len(expense)}")
        print("-"*20)
    elif option==5:
        while True:
            index=0
            print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
            print("-"*36)
            while index<len(expense):
                print(f"{index}. {expense[index]['Category']:<12}{expense[index]['Amount']:<10}{expense[index]['Date']:<12}")
                index+=1
            print("-"*20)
            try:
                delete_index=int(input("Enter number to delete: "))
            except ValueError:
                print("Invalid input :(")
                print("-"*20)
                continue
            if 0<=delete_index<len(expense):    
                expense.pop(delete_index)
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print("Expense deleted successfully! ^_^")
                break
            else:
                print("Invalid number! Please enter correct number :(")    
            print("-"*20)
    elif option==6:
        with open("expenses.json","w") as file:
            json.dump([],file)
            expense=[]
        print(f"Expenses cleared successfully! ^_^")
        print("-"*20)    
    elif option==7:
        print(f"Program exited successfully! ^_^")
        print("-"*20)
        break
    else:
        print(f"Please enter correct option :(")
        print("-"*20)