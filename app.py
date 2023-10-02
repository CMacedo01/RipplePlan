# -- Import section --
from flask import Flask
from flask import render_template
import model
# from flask import request


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  month = model.get_month()
  year = model.get_year()
  weekday = model.get_weekday()
  day = model.get_day()
  list_days = model.list_days()
  test_case = model.test_case
  return render_template('index.html', month = month, year = year, weekday = weekday, day = day, list_days = list_days, test_case = test_case)








	
# This keeps us in debug mode so you don't have to constantly refresh
app.run(host='0.0.0.0', port=81, debug=True)