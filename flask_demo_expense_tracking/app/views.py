from app import app
from flask import render_template, request
from datetime import datetime
import pathlib
import os
import json
import glob



@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/trackExpense', methods=["GET", "POST"])
def trackExpense():
    if request.method == 'POST':
        amount = request.form.get('amount')
        for_what = request.form.get('for_what')
        expense_date = request.form.get('expense_data')
        if expense_date:
            record_date = expense_date
        else:
            record_date = datetime.now().date().strftime('%Y-%m-%d')
        data = {'amount': amount, 'for_what': for_what, 'record_date': record_date}
        file_name = datetime.now().strftime('%Y%m%d_%H%M%S') + '.json'
        cur_file_path = pathlib.Path(__file__).parent.absolute()
        output_dir = os.path.join(cur_file_path, 'tracking_data')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, file_name)
        if not amount:
            return render_template('track_expense.html')

        with open(output_path, 'w') as f:
            f.write(json.dumps(data))
        return render_template('add_expense_success.html')
    return render_template('track_expense.html')

@app.route('/viewExpenses', methods=["GET"])
def viewExpenses():
    cur_file_path = pathlib.Path(__file__).parent.absolute()
    output_path = os.path.join(cur_file_path, 'tracking_data')

    expenses = []
    for filepath in glob.glob(os.path.join(output_path, '*.json')):
        with open(filepath) as f:
            content = json.load(f)
        expenses.append(content)
        print(content)

    return render_template('view_expenses.html', expenses=expenses)
