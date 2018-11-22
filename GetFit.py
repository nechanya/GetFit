from flask import Flask
from flask import render_template

app = Flask(__name__)\

@app.route('/')
def first():
    return render_template('page_getfit.html')

@app.route('/menu')
def second():
    return render_template('get_fit_menu.html')

@app.route('/user/<username>')
def user_page(username):
    return render_template('page_getfit.html', user=username)

@app.route('/diary')
def diary():
    return render_template('page_diary.html')

@app.route('/anketa')
def anketa():
    return 'Tell us about you and we will match you with the team!'

@app.route('/selecting')
def selecting():
    return 'Wait a second: we are selecting the participants for your team!'

if __name__== '__main__':
    app.run()


