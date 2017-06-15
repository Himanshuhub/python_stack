from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  # print request.form
  return render_template('result.html', name1= name, location = location, language = language, comment = comment)
  # return redirect('result.html')

app.run(debug=True)
