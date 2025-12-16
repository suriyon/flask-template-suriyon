from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Suriyon Saramul'
  email = 'suriyon.s@ubru.ac.th'
  mobile = '089-826-4842'
  age = 49
  return render_template('about.html', 
                         title=title,
                         name=name,
                         email=email,
                         mobile=mobile,
                         age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['หมูทอดกระเทียม', 'ก๋วยเตี๋ยวต้มยำ', 'กระเพราไก่+ไข่ดาว']
  return render_template('favorite_foods.html',
                         title=title,
                         foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite Sports Page'
  sports = ['Soccer', 'Baseball', 'Basketball', 'American Football', 'Ice Hockey']
  return render_template('favorite_sports.html',
                         title=title,
                         sports=sports)