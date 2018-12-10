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




@app.route('/sign_in', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['login'] = request.form.get('login')
        user['password'] = request.form.get('password')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users_sign_in where login='%s'" % user['login'])
        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO users_sign_in "
                      "(login, password) "
                      "VALUES "
                      "('{login}','{password}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        # return redirect('/user/%s/' % user['login'])


    return render_template(
        "get_fit_sign_in.html",
        user_created=user_created,
        error_message=error_message
    )

@app.route('/sign_up', methods=['GET', 'POST'])
def new_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['login'] = request.form.get('login')
        user['password'] = request.form.get('password')
        user['first_name'] = request.form.get('first_name')
        user['last_name'] = request.form.get('last_name')
        user['sex'] = request.form.get('sex')
        user['city'] = request.form.get('city')
        user['weight_now'] = request.form.get('weight_now')
        user['desired_weight'] = request.form.get('desired_weight')
        user['height'] = request.form.get('height')
        user['age'] = request.form.get('age')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM info_about_users where login='%s'" % user['login'])
        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO info_about_users"
                      "(login, password, first_name, last_name, sex, city, weight_now, desired_weight, height, age)"
                      "VALUES "
                      "('{login}','{password}','{first_name}','{last_name}','{sex}','{city}','{weight_now}','{desired_weight}','{height}','{age}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        # return redirect('/user/%s/' % user['login'])


    return render_template(
        "get_fit_registration.html",
        user_created=user_created,
        error_message=error_message
    )




if __name__ == "__main__":
    app.run()


