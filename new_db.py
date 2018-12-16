
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
    weight_now INTEGER,
    desired_weight INTEGER,
    height INTEGER,
    age INTEGER,
    vegetarian INTEGER,
    allergy_lactose INTEGER,
    allergy_oranges INTEGER,
    allergy_gluten INTEGER,
    
    FOREIGN KEY (login) REFERENCES users_sign_in(login) 
)
''')

conn.commit()

c.execute('''
CREATE TABLE diet_advice (
    advice_id INTEGER PRIMARY KEY AUTOINCREMENT,

    info TEXT,
    has_meat INTEGER,
    has_lactose INTEGER,
    has_oranges INTEGER,
    has_gluten INTEGER

)
''')

conn.commit()

c.execute('''
CREATE TABLE exercise_advice (
    advice_id INTEGER PRIMARY KEY AUTOINCREMENT,
  
    info TEXT,

    FOREIGN KEY (login) REFERENCES users_sign_in(login) 
)
''')

conn.commit()




users = [
    {
        'login': 1507,
        'password': 000,
        'first_name': 'Polina',
        'last_name': 'Yarovaya',
        'sex': 'w',
        'weight_now': 53,
        'desired_weight': 50,
        'height': 170,
        'age': 20,
        'vegetarian': 1,
        'allergy_lactose': 0,
        'allergy_oranges': 0,
        'allergy_gluten': 1

    },
    {
        'login': 1309,
        'password': 100,
        'first_name': 'Dasha',
        'last_name': 'Mikhalchuk',
        'sex': 'w',
        'weight_now': 55,
        'desired_weight': 50,
        'height': 160,
        'age': 20,
        'vegetarian': 0,
        'allergy_lactose': 1,
        'allergy_oranges': 0,
        'allergy_gluten': 1

    },
    {
        'login': 1712,
        'password': 010,
        'first_name': 'Anna',
        'last_name': 'Bushmeleva',
        'sex': 'w',
        'weight_now': 55,
        'desired_weight': 49,
        'height': 165,
        'age': 19,
        'vegetarian': 1,
        'allergy_lactose': 1,
        'allergy_oranges': 1,
        'allergy_gluten': 0

    }

]


food = [
           {
               'advice_id': '1',
               'info': 'White Bean, Herb Hummus with Crudites.Combine beans, chives, lemon juice, and oil in a small bowl. Mash with a fork until smooth. Serve with 1/2 cup raw vegetables, such as cucumbers, carrots, sugar snap peas, bell peppers, broccoli, and grape tomatoes',
               'has_meat': 0,
               'has_lactose': 0,
               'has_oranges': 1,
               'has_gluten': 0
           },
           {
               'advice_id': '2',
               'info': 'Middle Eastern Rice Salad.Heat oil in a large nonstick skillet over medium-high heat. Add onion, and cook, stirring often, about 5 minutes or until onion begins to brown. Remove from heat, and stir in chickpeas, cumin, and salt. Season to taste with freshly ground black pepper. Combine rice, onion-chickpea mixture, dates, mint, and parsley in a large bowl. Toss well until thoroughly combined. Serve warm or at room temperature.',
               'has_meat': 0,
               'has_lactose': 0,
               'has_oranges': 0,
               'has_gluten': 0
           },
    {
        'advice_id': '3',
        'info': 'Black Bean and Chicken Chilaquiles. Heat a large nonstick skillet over medium-high heat. Coat pan with cooking spray. Add onion; saut 5 minutes or until lightly browned. Add garlic; saut 1 minute. Add chicken; cook 30 seconds. Transfer mixture to a medium bowl; stir in beans. Add broth and salsa to pan; bring to a boil. Reduce heat, and simmer 5 minutes, stirring occasionally. Set aside. Place half of tortilla strips in bottom of an 11 x 7-inch baking dish coated with cooking spray. Layer half of chicken mixture over tortillas; top with remaining tortillas and chicken mixture. Pour broth mixture evenly over chicken mixture.',
        'has_meat': 1,
        'has_lactose': 1,
        'has_oranges': 0,
        'has_gluten': 0
    },
           {
               'advice_id':'4',
               'info': 'Creamy Avocado Cups.Peel, pit, and mash 1 avocado; set aside. Combine 1 tablespoon lime juice, 1 tablespoon reduced-fat sour cream or plain yogurt, 1/4 teaspoon ground cumin, and 1 tablespoon chopped fresh cilantro in a small bowl; stir in avocado. Spoon avocado mixture evenly into 12 endive leaves.',
               'has_meat':'0',
               'has_lactose':'1',
               'has_oranges':'1',
               'has_gluten':'0'
           },
    {
        'advice_id': '5',
        'info': 'Banana-Nut Oatmeal.Combine oats and 1 cup water in a small microwave-safe bowl. Microwave at HIGH 3 minutes. Top with banana slices, walnuts, and cinnamon. Carb Star: Oatmeal 6 grams of Resistant Starch per 1/2 cup raw or toasted oats Oatmeal for breakfast might help you eat less all day. In a series of experiments, researchers in Italy replaced the flour in bread and pasta with oats. They found that even when these foods had identical calorie counts, oat eaters consumed fewer calories over the course of the day.',
        'has_meat': 0,
        'has_lactose': 0,
        'has_oranges': 0,
        'has_gluten': 1
    },
           {
               'advice_id': '6',
               'info': 'BBQ Turkey Burgers.In medium bowl, gently mix together turkey, garlic, paprika, and cumin. Form turkey into 4 (4-inch) patties; season with salt and pepper. Heat grill to medium-high; cook, turning once, until burgers are just cooked through (about 7 minutes per side). Serve with desired toppings and buns.',
               'has_meat': 1,
               'has_lactose': 0,
               'has_oranges': 0,
               'has_gluten': 1
           },
           {
               'advice_id': '7',
               'info': 'Curried Egg Salad Sandwich.Combine eggs, yogurt, bell pepper, curry powder, salt, and pepper, in a small bowl; stir well. Place spinach on rye bread, top with egg salad, and serve the orange on the side.',
               'has_meat': 0,
               'has_lactose': 0,
               'has_oranges': 0,
               'has_gluten': 1
           },
]


for user in users:
    c.execute("INSERT INTO info_about_users"
              "(login, password, first_name, last_name, sex, weight_now, desired_weight, height, age, vegetarian, allergy_lactose, allergy_oranges, allergy_gluten)"
              "VALUES "
              "('{login}','{password}','{first_name}','{last_name}','{sex}','{weight_now}','{desired_weight}','{height}','{age}', {vegetarian}, {allergy_lactose}, {allergy_oranges}, {allergy_gluten})"
              "".format(**user))

    conn.commit()


for f in food:
    c.execute("INSERT INTO diet_advice"
              "( advice_id, info,has_meat, has_lactose ,has_oranges,has_gluten)"
              "VALUES "
              "({advice_id}, '{info}', {has_meat}, {has_lactose} ,{has_oranges},{has_gluten})"
              "".format(**f))
conn.commit()

c.execute("SELECT * "
          "FROM info_about_users "
          )
conn.close()
