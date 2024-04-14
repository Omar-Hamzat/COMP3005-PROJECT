"""
Name: Omar Hamzat
Student Number: 101244220
date: 13th April 2024
"""
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from database import *
from datetime import datetime, time
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'key'

# Function to connect to the database
"""
Please Update the database name, port #, user and password
"""
def connect_db():
    try:
        conn = psycopg2.connect(
            database="COMP3005_PROJECT",
            user="postgres",
            password="Hamzat1970!",
            host="localhost",
            port='5432'
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    account_type = request.form['account_type']
    password = request.form['password']
    print(account_type)
    # Redirect to appropriate page based on account type
    if account_type == 'member':
        members = get_members()
        for m in members:
            print(m)
            if m[1] == username:
                print(m[1], m[2])
                if m[2] == password:
                    return redirect(url_for('member_dashboard', username=username))
    elif account_type == 'trainer':
        trainers = get_trainers()
        for trainer in trainers:
            if trainer[1] == username and trainer[2] == password:
                return redirect(url_for('trainer_dashboard', username=username))
    elif account_type == 'staff':
        admins = get_admin()
        for admin in admins:
            if admin[1] == username and admin[2] == password:
                return redirect(url_for('admin_dashboard', username=username))
    return "Invalid account type"

@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        address = request.form['address']

        # Check if the username already exists in the database
        existing_members = get_members()
        for member in existing_members:
            if member[1] == username:
                return "Username already exists. Please choose a different username."

        # Create a new member
        new_member = (username, password, address)

        try:
            conn = connect_db()
            cursor = conn.cursor()

            sql = """INSERT INTO members (username, password, address) VALUES (%s, %s, %s)"""
            cursor.execute(sql, new_member)
            conn.commit()

            return redirect(url_for('index'))
        except (Exception, psycopg2.Error) as error:
            print("Error while adding new member:", error)
            return "Error while adding new member. Please try again later."
        finally:
            if conn:
                cursor.close()
                conn.close()

    return render_template('signup.html')

@app.route('/member_dashboard/<username>')
def member_dashboard(username):
    members = get_members()
    for m in members:
        if m[1] == username:
            member_info = m

    trainers = get_trainers()
    health_metrics = get_health_metrics(username)
    fitness_goals = get_fitness_goals(username)
    return render_template('dashboard.html', username=username, member_info=member_info, trainers=trainers, health_metrics=health_metrics, fitness_goals=fitness_goals)

# Route to display members
@app.route('/members')
def members():
    conn = connect_db()
    members_data = []

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM members")
            members_data = cur.fetchall()

        except psycopg2.Error as e:
            print("Error fetching members:", e)
        finally:
            cur.close()
            conn.close()

    return render_template('members.html', members_data=members_data)


@app.route('/add_health_metric/<username>', methods=['POST'])
def add_health_metric(username):
    metric_name = request.form['metric_name']
    weight = request.form['weight']
    height = request.form['height']
    pressure = request.form['pressure']
    rate = request.form['rate']

    # Add the health metric to the database (You'll need to implement this function)
    add_health_metric_to_db(username, metric_name, weight, height, pressure, rate)

    # Redirect back to the dashboard
    return redirect(url_for('member_dashboard', username=username))


@app.route('/book_training_session/<username>', methods=['POST'])
def book_training_session(username):
    trainer_id = request.form['trainer']
    date = request.form['date']
    time = request.form['time']

    # Book the training session in the database (You'll need to implement this function)
    book_training_session_to_db(username, trainer_id, date, time)

    # Redirect back to the dashboard
    return redirect(url_for('member_dashboard', username=username))

@app.route('/add_fitness_goals/<username>', methods=['POST'])
def add_fitness_goals(username):
    target_weight = request.form['target_weight']
    target_time = request.form['target_time']
    cardio_records = request.form['cardio_records']
    weightlifting_goals = request.form['weightlifting_goals']

    # Add the fitness goals to the database (You'll need to implement this function)
    add_fitness_goals_to_db(username, target_weight, target_time, cardio_records, weightlifting_goals)

    # Redirect back to the dashboard
    return redirect(url_for('member_dashboard', username=username))


@app.route('/trainer_dashboard/<username>')
def trainer_dashboard(username):
    trainers = get_trainers()
    trainer_id = get_trainer_id(username)
    for m in trainers:
        if m[1] == username:
            trainers = m
    available_times = get_available_times(username)
    members = get_members_for_trainer(trainer_id)
    return render_template('trainer-dashboard.html', username=username, trainers=trainers, available_times=available_times, members=members)

@app.route('/trainers')
def trainers():
    conn = connect_db()
    trainers_data = []

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM trainers")
            trainers_data = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching trainers:", e)
        finally:
            cur.close()
            conn.close()

    return render_template('trainers.html', trainers_data=trainers_data)


@app.route('/edit_availability/<username>')
def edit_availability(username):
    return render_template('edit-availability.html', username=username)


@app.route('/save_availability/<username>', methods=['POST'])
def save_availability(username):
    day = request.form['day']
    start_time = request.form['start_time']
    end_time = request.form['end_time']

    # Save the availability to the database (You'll need to implement this function)
    save_availability_to_db(username, day, start_time, end_time)

    # Redirect back to the dashboard or a confirmation page
    return redirect(url_for('trainer_dashboard', username=username))


@app.route('/admin_dashboard/<username>')
def admin_dashboard(username):
    admin = get_admin()
    for m in admin:
        if m[1] == username:
            admin = m

    members = get_members()
    return render_template('admin-dashboard.html', username=username, admin=admin, members=members)

@app.route('/manage_equipment')
def manage_equipment():
    conn = connect_db()
    equipment_data = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT name, COUNT(*) as total, SUM(CAST(functionality_status AS int)) as faulty FROM equipment GROUP BY name")
            equipment_data = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching equipment data:", e)
        finally:
            cur.close()
            conn.close()

    return render_template('monitor-equipment.html', equipment_data=equipment_data)


@app.route('/classes')
def classes():
    conn = connect_db()
    classes_data = []

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM classes")
            classes_data = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching classes:", e)
        finally:
            cur.close()
            conn.close()

    return render_template('class-list.html', classes_data=classes_data)

@app.route('/payroll_profiles')
def payroll_profiles():
    conn = connect_db()
    profiles = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM payroll_profile")
            profiles = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching payroll profiles:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Error connecting to database.")

    print("Fetched profiles:", profiles)  # Check if profiles is empty or contains data
    return render_template('payroll_profiles.html', profiles=profiles)

@app.route('/process_payment/<int:id>', methods=['POST'])
def process_payment(id):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE payroll_profile SET paid = true WHERE id = %s", (id,))
            conn.commit()
        except psycopg2.Error as e:
            print("Error updating payment status:", e)
        finally:
            cur.close()
            conn.close()
    return redirect(url_for('payroll_profiles'))





if __name__ == '__main__':
    app.run(debug=True)
