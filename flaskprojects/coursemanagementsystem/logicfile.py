import psycopg2
from flask import *

app = Flask(__name__)
app.secret_key = '123'

def create_table():
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='admin',
        host='127.0.0.1', port='5433'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    print("Table created successfully........")
    conn.close()

create_table()

@app.route('/StudentHomepage')
def Student_Homepage():
    # data = StudentHomepage()
    #return render_template("student/StudentHomepage.html", data=data)
    if 'user_id' in session:
        return render_template("faculty/FacultyHomepage.html")
    else:
        return redirect(url_for('loginpagecall'))

@app.route('/')
def index():
    return render_template("project/ProjectHomepage.html")



@app.route('/FacultyHomepage')
def FacultyHomepage():
    # Check if the user is logged in
    if 'user_id' in session:
        return render_template("faculty/FacultyHomepage.html")
    else:
        return redirect(url_for('loginpagecall'))

@app.route('/signuppagecall')
def signuppagecall():
    return render_template('project/Signup.html')

@app.route('/signup', methods=['POST'])
def signuplogic():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phone_number']

    # Insert user into the database
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='admin',
        host='127.0.0.1', port='5433'
    )
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO users (username, password, email, phone_number)
            VALUES (%s, %s, %s, %s)
        ''', (username, password, email, phone_number))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/loginpagecall')
def loginpagecall():
    return render_template('project/Login.html')

@app.route('/loginlogic', methods=['POST'])
def loginlogic():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = psycopg2.connect(
            database="CMS", user='postgres',
            password='admin',
            host='127.0.0.1', port='5433'
        )
        cursor = conn.cursor()

        cursor.execute('''
                    SELECT * FROM users WHERE username=%s AND password=%s
                ''', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            if len(username) == 4:
                return redirect(url_for('FacultyHomepage'))
            elif len(username) == 10:  # Assume student username has 10 digits
                return redirect(url_for('Student_Homepage'))
            else:
                # Redirect to a default page or handle other cases
                return redirect(url_for('index'))
        else:
            return render_template('project/Login.html', error='Invalid username or password')

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear the user_id from the session
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
