from flask import Flask
from flask import render_template


app = Flask(__name__)\

@app.route('/')
def hello():
    return render_template('page0.html')\

@app.route('/anketa')
def anketa():
    return 'Tell us about you and we will match you with the team!'\

@app.route('/selecting')
def selecting():
    return 'Wait a second: we are selecting the participants for your team!'

@app.route('/user/<username>')
def user_page(username):
    return render_template('page0.html', user=username)

if __name__== '__main__':
    app.run()


