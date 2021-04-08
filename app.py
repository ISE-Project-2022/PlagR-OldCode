import os
import werkzeug
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == '' and form.password.data == '':
            flash(f'Logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route("/home/")
def home():
    return render_template('home.html', title='Home')

@app.route("/pairwisecomparison/", methods=['GET', 'POST'])
def PCTool():
    #Define method used to get files
    if request.method == "POST":
        #assign names to files
        reported_file = request.files.getlist("Reported_Document")
        suspected_files = request.files.getlist("Suspected_Documents")
        #read everyline in each file
        for file in reported_file:
             reported = file.readlines()
        for file in suspected_files:
             suspects = file.readlines()
             #Shows output of each file
             return render_template('pairwisecomparison.html', title='Pairwise Comparison', reported=reported, suspects=suspects)
    #returns original page
    return render_template('pairwisecomparison.html', title='Pairwise Comparison')

@app.route("/stylometricclustering/")
def SCTool():
    return render_template('stylometricclustering.html', title='Stylometric Clustering')

@app.route("/help/")
def help():
    return render_template('help.html', title='Help')


if __name__ == '__main__':
    app.run(debug=True)