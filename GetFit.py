from flask import Flask
from flask import render_template
import db
import sqlite3
from flask import request

app = Flask(__name__)

@app.route('/list')
def user_list():
    conn = sqlite3.connect('new_db')
    c=conn.cursor()
    c.execute("SELECT * FROM info_about_users ")
    users=list(c.fetchall())
    conn.close()
    return render_template('page01.html', users=users)


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
def personal():
    return render_template('get_fit_personal.html')


@app.route('/diary')
def diary():
    return render_template('page_diary.html')

@app.route('/grouppage')
def grouppage():
    return render_template('get_fit_grouppage.html')


@app.route('/result')
def search_for_person():
    q=request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('page01.html', q=q, users=users)



@app.route('/user/<username>')
def get_user(username):
    return render_template('page01.html', name=username)

if __name__ == "__main__":
    app.run()


