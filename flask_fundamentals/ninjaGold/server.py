from flask import Flask ,render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template('index.html')    # Render the template and return it!

@app.route('/process', methods =['POST'])
def process():
  session['building'] = request.form['building']
  if session.get('gold') == None:
    session['gold'] = 0
    return redirect('/')
  if request.form['building'] == "farm":
    session['gold'] += random.randint(10,20)
    return redirect('/')
  if request.form['building'] == "cave":
    session['gold'] += random.randint(5,10)
    return redirect('/')
  if request.form['building'] == "house":
    session['gold'] += random.randint(2,5)
    return redirect('/')
  if request.form['building'] == "casino":
    session['gold'] += random.randint(-50,50)
    return redirect('/')
  print session['gold']
  return redirect('/')

app.run(debug=True)                       # Run the app in debug mode.
