from flask import Flask
from flask import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/a')
def hello1():
    return 'Hello, World!'

@app.route('/emp/<int:emp1>')
def show_emp(emp1):
  return 'EMP id number %d' %emp1

@app.route('/emp/<float:emp1>')
def show_emp1(emp1):
  return 'EMP id number %f' %emp1

@app.route('/ex1')
def index():
    return render_template('hello.html')



if __name__ == "__main__":
    app.run(debug=True)