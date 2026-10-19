import mysql.connector


try:
    # First connect without database to create it
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"  # Your MySQL password
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    print("Database student_db ready")
    conn.close()

    # Now connect to student_db
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="student_db"
    )
    cursor = conn.cursor()

    # Create tables if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT, course VARCHAR(50), marks INT)")
    
    # Insert admin user if not exists
    cursor.execute("INSERT IGNORE INTO users VALUES ('admin', 'admin123')")
    conn.commit()
    
    print("Connected to student_db successfully!\n")

except Exception as e:
    print(f"Database Error: {e}")
    exit()


def login():
    print("===== Admin Login Required =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check from database
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    if result:
        print("\nLogin Successful! Welcome admin.\n")
        return True
    else:
        print("\nInvalid Username or Password! Try admin / admin123")
        return False

# Check login before showing menu
if not login():
    conn.close()
    exit()

# --- 3. SHOWING EXISTING MENU ---
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))
        cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)", (name, age, course, marks))
        conn.commit()
        print("Student Added!\n")

    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
        print()

    elif choice == '3':
        print("Bye Arya!")
        break
    else:
        print("Invalid choice\n")

conn.close()
