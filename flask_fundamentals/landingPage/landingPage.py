from flask import Flask ,render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html')    # Render the template and return it!

# /projects
@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')    # Render the template and return it!

@app.route('/dojos')
def dojos():
  return render_template('dojos.html')    # Render the template and return it!

@app.route('/dojos', methods = ['POST'])
def create_user():
  name = request.form['name']
  email = request.form['email']
  return redirect('/')    # Render the template and return it!

app.run(debug=True)                       # Run the app in debug mode.
