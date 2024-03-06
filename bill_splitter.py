def bill_splitter():
    # Step 1: Collect Input
    total_amount = float(input("Enter the total amount of the bill: "))
    num_people = int(input("Enter the number of people: "))
    people = []
    for i in range(num_people):
        name = input(f"Enter the name of person {i+1}: ")
        people.append(name)

    # Step 2: Enter Individual Expenses
    expenses = []
    for person in people:
        expense = float(input(f"Enter the total expenses for {person}: "))
        expenses.append({"person": person, "expense": expense})

    # Step 3: Calculate Share
    total_expense = sum(expense["expense"] for expense in expenses)
    equal_share = total_expense / num_people

    # Step 4: Calculate Owed Amount
    owed_amounts = []
    for expense in expenses:
        owed_amount = expense["expense"] - equal_share
        owed_amounts.append({"person": expense["person"], "owed_amount": owed_amount})

    # Step 5: Display Results
    print("\nExpense Summary:")
    for owed_amount in owed_amounts:
        person = owed_amount["person"]
        amount = owed_amount["owed_amount"]
        if amount > 0:
            print(f"{person} owes {amount:.2f}")
        elif amount < 0:
            print(f"{person} is owed {-amount:.2f}")
        else:
            print(f"{person} has no dues.")


bill_splitter()
