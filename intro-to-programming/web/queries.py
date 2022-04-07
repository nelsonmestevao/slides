import sqlite3

connection = sqlite3.connect("company.db")

cursor = connection.cursor()

rows = cursor.execute("SELECT first_name, last_name, salary FROM employees").fetchall()

print(rows)

for (first_name, _, _) in rows:
    print(first_name)
