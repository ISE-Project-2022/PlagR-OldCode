from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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

@app.route("/pairwisecomparison/")
def PCTool():
    return render_template('pairwisecomparison.html', title='Pairwise Comparison')

@app.route("/stylometricclustering/")
def SCTool():
    return render_template('stylometricclustering.html', title='Stylometric Clustering')

@app.route("/help/")
def help():
    return render_template('help.html', title='Help')


if __name__ == '__main__':
    app.run(debug=True)