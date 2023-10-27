from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bill_splitter():
    if request.method == 'POST':
        total_amount = float(request.form['total_amount'])
        num_people = int(request.form['num_people'])
        people = []
        for i in range(num_people):
            name = request.form[f'person_{i + 1}']
            people.append(name)

        expenses = []
        for person in people:
            expense = float(request.form[f'expense_{person}'])
            expenses.append({"person": person, "expense": expense})

        total_expense = sum(expense["expense"] for expense in expenses)
        equal_share = total_expense / num_people

        owed_amounts = []
        for expense in expenses:
            owed_amount = expense["expense"] - equal_share
            owed_amounts.append({"person": expense["person"], "owed_amount": owed_amount})

        creditors = [owed for owed in owed_amounts if owed["owed_amount"] > 0]
        debtors = [owed for owed in owed_amounts if owed["owed_amount"] < 0]

        transactions = []
        for debtor in debtors:
            debtor_name = debtor["person"]
            debtor_amount = abs(debtor["owed_amount"])

            while debtor_amount > 0:
                creditor = min(creditors, key=lambda x: x["owed_amount"])

                creditor_name = creditor["person"]
                creditor_amount = creditor["owed_amount"]

                # if debtor_amount >= abs(creditor_amount):
                #     transaction_amount = abs(creditor_amount)
                #     debtor_amount -= transaction_amount
                #     creditor_amount += transaction_amount
                #     creditors.remove(creditor)
                else:
                    transaction_amount = debtor_amount
                    debtor_amount = 0
                    creditor_amount += transaction_amount

                transactions.append({"from": debtor_name, "to": creditor_name, "amount": transaction_amount})

        return render_template('results.html', transactions=transactions)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
