from flask import Flask ,render_template

app = Flask(__name__)
@app.route('/')
def root():
  return render_template('index.html')    # Render the template and return it!

# /projects
@app.route('/projects')
def projects():
  return render_template('projects.html')    # Render the template and return it!

# /about
@app.route('/about')
def about():
  return render_template('about.html')    # Render the template and return it!

app.run(debug=True)                       # Run the app in debug mode.
