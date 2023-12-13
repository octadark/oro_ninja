from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    place = request.form['place']

    if place == 'farm':
        gold_earned = random.randint(10, 20)
    elif place == 'cave':
        gold_earned = random.randint(5, 10)
    elif place == 'house':
        gold_earned = random.randint(2, 5)
    elif place == 'casino':
        gold_earned = random.randint(-50, 50)

    session['gold'] += gold_earned
    session['activities'].append(f'Earned {gold_earned} gold from the {place}!')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 