from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def bill_splitter():
    transactions = []
    if request.method == 'POST':
        # total_amount = float(request.form['total_amount'])
        # num_people = int(request.form['num_people'])
        num_people = 3
        people = []
        for i in range(num_people):
            name = request.form[f'person_{i + 1}']
            people.append(name)
        print(people)
        expenses = []
        
        for i, person in enumerate(people):
            expense = float(request.form[f'expense_person_{i + 1}'])
            expenses.append({"person": person, "expense": expense})
           
        print(expenses)
        total_expense = sum(expense["expense"] for expense in expenses)

        equal_share = total_expense / num_people
        
        owed_amounts = []
        for expense in expenses:
            owed_amount = expense["expense"] - equal_share
            owed_amount = round(owed_amount,2)
            owed_amounts.append({"person": expense["person"], "owed_amount": owed_amount})

        creditors = [owed for owed in owed_amounts if owed["owed_amount"] > 0]
        debtors = [owed for owed in owed_amounts if owed["owed_amount"] < 0]
        print(f"CREDITOR:::::{creditors}")
        print(f"DEBTOR:::::{debtors}")
        
        
        for debtor in debtors:
            debtor_name = debtor["person"]
            debtor_amount = abs(debtor["owed_amount"])

            while debtor_amount > 0:
                creditor = min(creditors, key=lambda x: x["owed_amount"])
                # def get_owed_amount(creditor):
                #     return creditor["owed_amount"]                
                # creditor = min(creditors, key=get_owed_amount)
                
                creditor_name = creditor["person"]
                creditor_amount = creditor["owed_amount"]

                if debtor_amount >= abs(creditor_amount):
                    transaction_amount = abs(creditor_amount)
                    debtor_amount -= transaction_amount
                    creditor_amount += transaction_amount
                    creditors.remove(creditor)
                else:
                    transaction_amount = debtor_amount
                    transaction_amount= round(transaction_amount,2)
                    debtor_amount = 0
                    creditor_amount += transaction_amount

                transactions.append({"from": debtor_name, "to": creditor_name, "amount": transaction_amount})

        # return render_template('results.html', transactions=transactions)

        return render_template('index2.html',  transactions=transactions)
    else:
        # Clear the transactions list for a new page load
        transactions.clear()
        return render_template('index2.html',  transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)