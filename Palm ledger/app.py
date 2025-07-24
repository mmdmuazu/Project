# Directory structure:
# palm_ledger_app/
# ├── app.py
# ├── templates/
# │   └── index.html
# └── static/
#     ├── style.css
#     └── script.js

# ===== app.py =====
from flask import Flask, render_template, request, redirect, url_for,jsonify
from datetime import datetime
# from flask_cors import CORS

app = Flask(__name__)
from flask import Flask, render_template, request, redirect
from datetime import datetime
from json import load,dump

app = Flask(__name__)

# Sample in-memory data store
try:
    with open("./document.json",'r') as db:
        ledger = load(db) 
except Exception:
     ledger =[]
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['customer_name']
        product = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        paid = request.form.get('paid')
        is_paid = paid == "on"
        print(paid)
        total = quantity * price
        timestamp = datetime.now().strftime('%b %d, %Y %I:%M %p')

        ledger.append({
            "customer_name": name,
            "product_name": product,
            "quantity": quantity,
            "price": price,
            "total": total,
            "date": timestamp,
            "paid": is_paid,
            "color":"green" if is_paid else "red"
        })
        with open('./document.json','w') as doc:
            dump(ledger,doc)
        # for i in ledger:
        #     print("find",i)
        # print(ledger)
        # return redirect('/')

    # Handle search query
    query = request.args.get('search')
    if query:
        filtered = [item for item in ledger if query.lower() in item['customer_name'].lower() or query.lower() in item['product_name'].lower()]
    else:
        filtered = ledger

    return render_template('test.html', ledger=filtered)

# transactions = []

# @app.route('/')
# def index():
#     # Handle search query
#     query = request.args.get('search')
#     if query:
#         filtered = [item for item in ledger if query.lower() in item['name'].lower() or query.lower() in item['product'].lower()]
#     else:
#         filtered = ledger
#     return render_template('index.html', transactions=transactions)

# @app.route('/add', methods=['POST'])
# def add_transaction():
#     data = {
#         'customer_name': request.form['customer_name'],
#         'product_name': request.form['product_name'],
#         'quantity': int(request.form['quantity']),
#         'price': float(request.form['price']),
#         'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
#     }
#     data['total'] = data['quantity'] * data['price']
#     transactions.append(data)
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

