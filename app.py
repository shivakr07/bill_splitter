from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bill_splitter():
    if request.method == 'POST':
        total_amount = float(request.form['total_amount'])
        num_people = int(request.form['num_people'])
        people = []
        for i in range(num_people):
            name = request.form.get(f'person_{i + 1}', '')
            people.append(name)

        expenses = []
        for person in people:
            expense = float(request.form.get(f'expense_{person}', '0'))
            expenses.append({"person": person, "expense": expense})

        total_expense = sum(expense["expense"] for expense in expenses)
        equal_share = total_expense / num_people

        owed_amounts = []
        for expense in expenses:
            owed_amount = expense["expense"] - equal_share
            owed_amounts.append({"person": expense["person"], "owed_amount": owed_amount})

        return render_template('results.html', owed_amounts=owed_amounts)

    return render_template('index.html', num_people=5) # Set num_people to a default value

if __name__ == '__main__':
    app.run(debug=True)
