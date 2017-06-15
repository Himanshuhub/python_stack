from flask import Flask,request, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "This is a secret!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def process():
    name = request.form['your_name']
    if len(str(name)) < 1:
        flash("Name cannot be empty, bruh!")
    else:
        print request.form['your_name']
        # flash("Success! Your name is {}".format(request.form['name']))
    dojo_location = request.form['dojo_location']
    if len(str(dojo_location)) < 1:
        flash("Dojo Location cannot be blank!")
    else:
        print request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    if len(str(favorite_language)) < 1:
        flash("Favorite Language cannot be blank!")
    else:
        print request.form['favorite_language']
    comment = request.form['comment']
    if len(str(comment)) < 1:
        flash("Comment cannot be empty, bruh!")
    if len(str(comment)) > 120:
        flash("Comment is way too long, bruh! No one wants to read a comment that long, bruh!")
    else:
        print request.form['comment']
        # flash("Success! Your comment works, bruh!")
    print name, dojo_location, favorite_language, comment
    return render_template('result.html', name=name, dojo_location=dojo_location, favorite_language=favorite_language, comment=comment)

app.run(debug=True)
