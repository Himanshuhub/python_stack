from flask import Flask ,render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')    # Render the template and return it!

@app.route('/', methods = ['POST'])
def create_user():
  name = request.form['name']
  return redirect('process.html')    # Render the template and return it!

@app.route('/process', methods = ['POST'])
def process():
  return render_template('process.html', name = request.form['name'])    # Render the template and return it!

app.run(debug=True)                       # Run the app in debug mode.
