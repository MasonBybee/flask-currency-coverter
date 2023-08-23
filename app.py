from flask import Flask, request, redirect, render_template, flash, jsonify, session, Response
import requests
from currency_codes import currency_codes

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

@app.route('/')
def home():
    return render_template('index.html')

def check_codes(codes):
    valid = True
    for code in codes:
        if code not in currency_codes:
            valid = False
            flash(f"Not a valid code: {code}", 'error')
    return valid

@app.route('/convert', methods=["POST"])
def convert_currency():
    form_data = request.form
    formatted_num = "0.00"
    amount = form_data.get('amount') or '100'
    from_code = form_data.get("from_currency") or "USD"
    to_code = form_data.get("to_currency") or 'EUR'
    if not check_codes([from_code, to_code]):
        return redirect('/')
    url = f'https://api.exchangerate.host/convert?from={from_code}&to={to_code}&amount={amount}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        formatted_num = f"{int(data['result']):,.2f}"
    else:
        flash('There was an error fetching the conversion.', 'error')
        return redirect('/')

    return render_template('result.html', num=formatted_num, currency=to_code)
