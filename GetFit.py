from flask import Flask
from flask import render_template
import db
from flask import request

app = Flask(__name__)\

@app.route('/')
def first():
    return render_template('page_getfit.html')

@app.route ('/sign_in')
def sign_in():
    return render_template('get_fit_sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('get_fit_registration.html')

@app.route('/personal')
def second():
    return render_template('get_fit_personal.html')


@app.route('/diary')
def diary():
    return render_template('page_diary.html')



@app.route('/result')
def search_for_person():
    q=request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('getfit_anketa.html', q=q, users=users)


@app.route('/selecting')
def selecting():
    return 'Wait a second: we are selecting the participants for your team!'\

@app.route('/user/<username>')
def get_user(username):
    return render_template('getfit_anketa.html', name=username)

if __name__ == "__main__":
    app.run()


