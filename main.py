import mysql.connector

# --- FIX: Auto-create database if not exists ---
# This uses your same password root123, no change
try:
    temp_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"  # YOUR SAME PASSWORD - DON'T CHANGE
    )
    temp_cursor = temp_conn.cursor()
    temp_cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    temp_conn.close()
    print("Database student_db ready")
except Exception as e:
    print(f"Temp connection error: {e}")

# --- Your original connection - Now it will work ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",  # SAME PASSWORD
    database="student_db"
)
cursor = conn.cursor()

# Create tables if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50),
    marks INT
)
""")
conn.commit()
print("Connected to student_db successfully!")

# --- Your rest of Student Management System code starts here ---
# Example menu (keep your existing code below this line)
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        marks = int(input("Marks: "))
        cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (%s,%s,%s,%s)", (name, age, course, marks))
        conn.commit()
        print("Student Added!")
    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
    elif choice == '3':
        break