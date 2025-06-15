# @app.route('/download', methods=['GET','POST'])
# def download_video():
#     if request.method == 'POST':
#         data = request.json
#         url = data.get('link')  # Get the video URL from the user
#         try:
#             # Use yt-dlp to get the direct download link
#             ydl_opts = {
#                 'username': os.getenv('YT_USERNAME'),  # Fetches from an environment variable
#                 'password': os.getenv('YT_PASSWORD'),
#                 'quiet': True,  # Suppress console output
#                 'format': 'best',  # Choose the best video format
#                 'verbose': True,
#                 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

#             }
#             with YoutubeDL(ydl_opts) as ydl:
#                 info = ydl.extract_info(url, download=False)  # Fetch info without downloading
#                 direct_url = info['url']  # Get the direct video URL

#             # Return the direct URL to the user
#             return jsonify({'message':'Done','link': str(direct_url)}),200

#         except Exception as e:
#             return jsonify({'message': str(e)}), 400
#     return render_template('index.html')
from flask import Flask, render_template, request,redirect, url_for, jsonify
from json import load, dump
import uuid
from yt_dlp import YoutubeDL
import os
app = Flask(__name__)
app.secret_key = b'muhammad!@#$%89878734jfd'

def get_username_by_referral_code(referral_code):
    for user_id, user in users.items():
        if user['referral_code'] == referral_code:
            return user_id

    return None
def get_username_by_address(user_address):
    for user_id, user in users.items():
        if user['address'] == user_address:
            username = user['username']
            return username
    return 'username not found'

try:
    with open('./users.db', 'r') as db:
        users = load(db)
except Exception:
    with open('./users.db', 'w') as db:
        users = {}
try:
    with open('./accounts.db', 'r') as db:
        accounts = load(db)
except Exception:
    with open('./accounts.db', 'w') as db:
        accounts = {}
try:
    with open('./transactions.db','r') as db:
        transactions = load(db)
except Exception:
    with open('./transactions.db','w') as db:
        transactions={}
@app.route("/")
def index():
    user_id = request.args.get("user_id")

    username = request.args.get("username")

    name = request.args.get("name")
    if username == 'None':
        if name:
            username = name
        else:
            return "<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USERNAME CAN'T BE NONE</h1>"

    if not username:
        if name:
           username = name
        else:
           return "<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USERNAME CAN'T BE NONE</h1>"

    if user_id == None:
        return "<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USER ID CAN'T BE NONE</h1>"
    if not user_id:
        return "<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USER ID CAN'T BE NONE</h1>"

    referral_code = request.args.get("referral_code")
    if user_id not in users:
        if referral_code:
            referrer_user_id = get_username_by_referral_code(referral_code)
            if referrer_user_id:
                users[referrer_user_id]['balance'] += 500
                users[referrer_user_id]['referred_users'].append(user_id)
            else:
                pass
        else:
            pass

        user_referral_code = str(uuid.uuid4().hex)[:6]
        address = str(uuid.uuid4().hex)[:60]
        users[user_id] = {
            'username': username,
            'referral_code': user_referral_code,
            'referred_by': referrer_user_id if referral_code else None,
            'referred_users': [],
            'links': [],
            'balance':0,
            "user_id":user_id,
            "address":address
        }

        accounts[address] = {
            'address':address,
            'balance': 0
        }

        with open('./users.db', 'w') as db:
            dump(users, db)
        db.close()
        with open('./accounts.db', 'w') as db:
            dump(accounts, db)
        db.close()
    return redirect(url_for("dashboard",userid=user_id))

@app.route('/dashboard/<userid>/')
def dashboard(userid):
    global usersid
    usersid = userid

    if usersid not in users:
        return "<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USER NOT REGISTERED</h1>"
    global user
    user = users.get(usersid, {})

    username = user["username"]


    referred_users = []
    for referred_user_id in user.get('referred_users', []):
        referred_user = users.get(referred_user_id, {})
        referred_username = referred_user["username"]
        referred_users.append({
            'username': referred_username,
            'balance': referred_user.get('balance', 0)
        })

    referral_link = f"https://t.me/Dollar_coin_mining_bot/?start={user.get('referral_code')}"
    global user_address
    user_address = user['address']
    address = accounts.get(user_address,{})
    dashboard_address = address["address"]
    userBalance = user['balance']

    if userBalance >= 10000:
        transfereble_balance = userBalance//10000*20
        user['balance'] -= userBalance
        accounts[user_address]['balance'] += transfereble_balance
        with open('./accounts.db', 'w') as db:
            dump(accounts,db)
        with open('./users.db', 'w') as db:
            dump(users,db)
    else:
       transfereble_balance = address['balance']
    sbalance = address['balance']

    return render_template('dashboard.html',
                           username=username,
                           balance=user.get('balance'),
                           referral_code=user.get('referral_code'),
                           referral_link=referral_link,
                           referred_users=referred_users,
                           dashboard_address=dashboard_address,
                           sbalance= sbalance
                           )

@app.route('/update_balance', methods=['POST'])
def update_balance():
    user_id = usersid
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    amount = data.get('amount', 1)

    try:
        amount = int(amount)
    except ValueError:
        return jsonify({'error': 'Invalid amount'}), 400

    if amount <= 0:
        return jsonify({'error': 'Amount must be positive'}), 400

    user['balance'] += amount
    with open('./users.db', 'w') as db:
        dump(users, db)
    db.close()

    return jsonify({'balance': user['balance']})

@app.route('/get_link_states')
def get_link_states():

    user_id = usersid
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    links = [{'href': link['href'], 'used': link['used']} for link in user['links']]
    return jsonify({'links': links})

@app.route('/mark_link_used', methods=['POST'])
def mark_link_used():
    user_id = usersid
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    href = data.get('href')

    for link in user['links']:
        if link['href'] == href:
            link['used'] = True
            break
    else:
        user['links'].append({'href': href, 'used': True})

    with open('./users.db', 'w') as db:
        dump(users, db)

    return jsonify({'success': True})
@app.route('/transfer', methods=['POST'])
def transfer():
    user = accounts.get(user_address,{})

    recipient_address = request.form.get('recipient_address')
    amount_str = request.form.get('amount')

    if not recipient_address or not amount_str:
        return jsonify({'success': False, 'message': 'Form data is missing.'}), 400
    try:
        amount = int(amount_str)
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid amount.'}), 400

    if amount <= 0:
        return jsonify({'success': False, 'message': 'Amount must be greater than 0.'}), 400

    if recipient_address not in accounts:
        return jsonify({'success': False, 'message': 'Recipient address does not exist.'}), 404

    if recipient_address == user_address:
        return jsonify({'success': False, 'message': 'Cannot transfer coins to your own account.'}), 400

    if user['balance'] < amount:
        return jsonify({'success': False, 'message': 'Insufficient funds.'}), 400

    transactions[user_address] = {
        'sender': user_address,
        'recipient': recipient_address,
        'amount': amount
        }
    with open('./transactions.db', 'w') as db:
        dump(transactions, db)
    accounts[user_address]['balance'] -= amount
    accounts[recipient_address]['balance'] += amount
    with open('./accounts.db', 'w') as db:
      dump(accounts, db)
    username = get_username_by_address(recipient_address)
    return jsonify({'success': True, 'message': f"Transfer successful: {amount} coins to {username} ✔"}), 200
@app.route('/airtime',methods=['POST'])
def airtime():
    data = request.json
    phone_number = data['phone_number']
    amount = int(data['airtime_amount'])
    if len(phone_number ) != 11:
        return jsonify({'error':True,'message':'phone number must be 11 digits'}),400
    if amount <= 99:
        return jsonify({'error':True,'message':'amount must be greater than 100'}),400
    return jsonify({'message':'good'})
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=False)