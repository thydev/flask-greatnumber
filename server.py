from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "sfj232dsf@#@#sfs329392"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['guessNumber'] != "":
            guess_num = int(request.form['guessNumber'])
        else:
            guess_num = 0

        if guess_num == session['mynum']:
            guess_status = 'win'
        elif guess_num < session['mynum']:
            guess_status = 'Too low!'
            session['guessed'] += 1
        else:
            guess_status = 'Too high!'
            session['guessed'] += 1

        return render_template('index.html', guess_status = guess_status, guess_num = guess_num)
    else:
        session.clear()
        if not 'mynum' in session:
            session['mynum'] = random.randint(1, 100)
            session['guessed'] = 0
            print session['guessed']
        return render_template('index.html')

@app.route('/replay', methods=['POST'])
def replay():
    session.pop('mynum')
    session.pop('guessed')
    return redirect('/')
app.run(debug = True)