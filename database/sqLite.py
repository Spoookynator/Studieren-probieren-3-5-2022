import sqlite3

conn = sqlite3.connect('database/example.db')

cursorObj = conn.cursor()

cursorObj.execute('DROP TABLE IF EXISTS employees')
cursorObj.execute("""CREATE TABLE employees(
    id integer PRIMARY KEY,
    name text,
    salary real,
    department text,
    position text,
    hireDate text)""")

cursorObj.execute(
    "INSERT INTO employees VALUES(14, 'John', 2700, 'IT', 'Manager', '2019-01-07')")

cursorObj.execute(
    "INSERT INTO employees VALUES(15, 'Jeremy', 2000, 'IT', 'Employee', '2015-02-07')")

cursorObj.execute(
    "INSERT INTO employees VALUES(16, 'Corry', 5000, 'MR', 'Employee', '2017-05-08')")

position = "Employee"

cursorObj.execute('SELECT * FROM employees WHERE position="'+position+'"')
all_rows = cursorObj.fetchall()

for p in all_rows:
    print (p)
    
conn.commit()

conn.close()