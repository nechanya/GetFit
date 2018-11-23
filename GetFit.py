from flask import Flask
from flask import render_template
import db
from flask import request

app = Flask(__name__)\

@app.route('/')
def first():
    return render_template('page_getfit.html')

@app.route('/menu')
def second():
    return render_template('get_fit_menu.html')


@app.route('/diary')
def diary():
    return render_template('page_diary.html')

@app.route('/anketa')
def anketa():
    return render_template('get_fit_registration.html')

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


