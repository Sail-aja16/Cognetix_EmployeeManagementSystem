import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    department TEXT,
    salary REAL
)
""")

def add_employee():
    id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    cursor.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(id,name,email,department,salary))
    conn.commit()
    print("Employee added successfully")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def search_employee():
    id = input("Enter Employee ID: ")

    cursor.execute("SELECT * FROM employees WHERE id=?",(id,))
    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Employee not found")

def delete_employee():
    id = input("Enter Employee ID to delete: ")

    cursor.execute("DELETE FROM employees WHERE id=?",(id,))
    conn.commit()
    print("Employee deleted")

while True:

    print("\n--- Employee Management System ---")
    print("1 Add Employee")
    print("2 View Employees")
    print("3 Search Employee")
    print("4 Delete Employee")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        break

    else:
        print("Invalid choice")
