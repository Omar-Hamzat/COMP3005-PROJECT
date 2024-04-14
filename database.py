"""
Name: Omar Hamzat
Student Number: 101244220
date: 13th April 2024
"""
import psycopg2

# Function to connect to the database
def connect_db():
    try:
        conn = psycopg2.connect(database="COMP3005_PROJECT", user="postgres", password="Hamzat1970!", host="localhost", port='5432')
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def register_member(first_name, last_name, email, password, address, phone):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """INSERT INTO Member (FirstName, LastName, Email, Password, Address, Phone)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (first_name, last_name, email, password, address, phone))
        conn.commit()
        print("Member registered successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while registering member:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_members():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM members"""
        cursor.execute(sql)
        members = cursor.fetchall()

        return members
    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving members:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_trainers():
    conn = connect_db()
    trainers = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM trainers")
            trainers = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching trainers:", e)
        finally:
             cur.close()
             conn.close()
    return trainers

def add_health_metric_to_db(username, metric_name, weight, height,pressure, rate):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO health_metrics (username, metric_name, weight, height, pressure, rate) VALUES (%s, %s, %s, %s, %s, %s)", (username, metric_name, height, weight, pressure, rate))
            conn.commit()
        except psycopg2.Error as e:
            print("Error inserting health metric:", e)
        finally:
            cur.close()
            conn.close()

def book_training_session_to_db(username, trainer_id, date, time):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO training_sessions (username, trainer_id, date, time) VALUES (%s, %s, %s, %s)", (username, trainer_id, date, time))
            conn.commit()
        except psycopg2.Error as e:
            print("Error booking training session:", e)
        finally:
            cur.close()
            conn.close()

def add_fitness_goals_to_db(username, target_weight, target_time, cardio_records, weightlifting_goals):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO fitness_goals (username, target_weight, target_time, cardio_records, weightlifting_goals) VALUES (%s, %s, %s, %s, %s)", (username, target_weight, target_time, cardio_records, weightlifting_goals))
            conn.commit()
        except psycopg2.Error as e:
            print("Error adding fitness goals:", e)
        finally:
            cur.close()
            conn.close()

def get_available_times(username):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT day_of_week, start_time, end_time FROM trainer_availability WHERE trainer_id = (SELECT id FROM trainers WHERE username = %s)", (username,))
            available_times = cur.fetchall()
            return available_times
        except psycopg2.Error as e:
            print("Error fetching available times:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []


def save_availability_to_db(username, day, start_time, end_time):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Check if the trainer's availability for the given day already exists
            cur.execute(
                "SELECT id FROM trainer_availability WHERE trainer_id = (SELECT id FROM trainers WHERE username = %s) AND day_of_week = %s",
                (username, day))
            existing_availability = cur.fetchone()
            if existing_availability:
                # Update the existing availability
                cur.execute("UPDATE trainer_availability SET start_time = %s, end_time = %s WHERE id = %s",
                            (start_time, end_time, existing_availability[0]))
            else:
                # Insert new availability
                cur.execute(
                    "INSERT INTO trainer_availability (trainer_id, day_of_week, start_time, end_time) VALUES ((SELECT id FROM trainers WHERE username = %s), %s, %s, %s)",
                    (username, day, start_time, end_time))

            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            print("Error saving availability to database:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to connect to the database")

def get_trainer_id(username):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM trainers WHERE username = %s", (username,))
            trainer_id = cur.fetchone()[0]
            return trainer_id
        except psycopg2.Error as e:
            print("Error getting trainer ID from database:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return None

def get_members_for_trainer(trainer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT username, date FROM training_sessions WHERE trainer_id = %s", (trainer_id,))
            members = cur.fetchall()
            return members
        except psycopg2.Error as e:
            print("Error getting members for trainer from database:", e)
            return []
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

def get_admin():
    conn = connect_db()
    admins = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM admin")
            admins = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching admin:", e)
        finally:
            cur.close()
            conn.close()
    return admins

def get_health_metrics(username):
    conn = connect_db()
    health_metrics = []

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM health_metrics WHERE username = %s", (username,))
            health_metrics = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching health metrics:", e)
        finally:
            cur.close()
            conn.close()

    return health_metrics

def get_fitness_goals(username):
    conn = connect_db()
    fitness_goals = []

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM fitness_goals WHERE username = %s", (username,))
            fitness_goals = cur.fetchall()
        except psycopg2.Error as e:
            print("Error fetching fitness goals:", e)
        finally:
            cur.close()
            conn.close()

    return fitness_goals





