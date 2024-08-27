from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
# mysql connection
cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "30696222",
    database = "hello_mysql"
)

# settings
app.secret_key = 'mysecretkey'


@app.route("/")
def Index():
    cur = cnn.cursor()
    cur.execute('SELECT * FROM new_tableuser')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        init_date = request.form['init_date']
        email = request.form['email']
        print(name)
        print(surname)
        print(age)
        print(init_date)
        print(email)
        try:
            cur = cnn.cursor()
            cur.execute('INSERT INTO new_tableuser (name, surname, age, init_date, email) VALUES (%s, %s, %s, %s, %s)',
                        (name, surname, age, init_date, email))
            cnn.commit()
            flash('Contact add susscefullly')
            return redirect(url_for('Index'))
        except:
            flash('Theres some error, try to add the contact again')
            return redirect(url_for('Index'))
        
@app.route('/edit/<string:user_id>')
def get_contact(user_id):
    cur = cnn.cursor()
    cur.execute(f'SELECT * FROM new_tableuser WHERE user_id = {user_id}')
    data = cur.fetchall()
    return render_template('edit_contact.html', contact = data[0])
    # flash('Contact edited successfully')
    # return redirect(url_for('Index'))

@app.route('/update/<user_id>', methods = ['POST'])
def update_contact(user_id):
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        init_date = request.form['init_date']
        email = request.form['email']
        cur = cnn.cursor()
        cur.execute(f'UPDATE new_tableuser SET name = %s, surname = %s, age = %s, init_date = %s, email = %s WHERE user_id = {user_id}', 
                    (name, surname, age, init_date, email))
        cnn.commit()
        flash('Contact Upadated susscefullly')
        return redirect(url_for('Index'))

@app.route('/delete/<string:user_id>')
def delete(user_id):
    cur = cnn.cursor()
    cur.execute(f'DELETE FROM new_tableuser WHERE user_id = {user_id}')
    cnn.commit()
    flash('Contact removed successfully')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(port= 3001, debug= True)