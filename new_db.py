
import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()

c.execute('''
CREATE TABLE users_sign_in (
    login INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    password TEXT
)
''')

conn.commit()



c.execute('''
CREATE TABLE info_about_users (
    login INTEGER UNIQUE PRIMARY KEY,
    password INTEGER,
    first_name TEXT,
    last_name TEXT,
    sex TEXT,
    city TEXT,
    weight_now INTEGER,
    desired_weight INTEGER,
    height INTEGER,
    age INTEGER,
    group_id INTEGER,
    FOREIGN KEY (login) REFERENCES users_sign_in(login) 
)
''')

conn.commit()

c.execute('''
CREATE TABLE group (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
  advice_id INTEGER
)
''')

conn.commit()

c.execute('''
CREATE TABLE diary_advice (
    advice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    login INTEGER,
    info TEXT,
    category TEXT,
    FOREIGN KEY (login) REFERENCES users_sign_in(login) 
)
''')

conn.commit()



c.execute('''
    INSERT INTO users_sign_in (login, password)
    VALUES ("1234", "pass")
''')

conn.commit()

users = [
    {
        'login': 'Polina',
        'password':'000',
        'first_name':'Polina',
        'last_name':'Yarovaya',
        'sex':'w',
        'city': 'Spb',
        'weight_now': '53',
        'desired_weight': '50',
        'height': '170',
        'age':'20'
    },

    {
        'login': 'Dasha',
        'password':'111',
        'first_name':'Dasha',
        'last_name':'Mikhachuk',
        's':'w',
        'city': 'Spb',
        'weight_now': '55',
        'desired_weight': '50',
        'height': '167',
        'age': '20'
    }
]

for user in users:
    c.execute("INSERT INTO info_about_users"
              "(login, password, first_name, last_name, sex, city, weight_now, desired_weight, height, age)"
              "VALUES "
              "('{login}','{password}','{first_name}','{last_name}','{sex}','{city}','{weight_now}','{desired_weight}','{height}','{age}')"
              "".format(**user))

    conn.commit()

c.execute("SELECT * "
          "FROM info_about_users "
          )
conn.close()
