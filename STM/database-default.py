import sqlite3
import time as t
print("Database checkpoint - Default check")
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT, name TEXT)")
cursor.execute("INSERT INTO users VALUES(1, 'Faisal')")
conn.commit()
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
t.sleep(4)
print("Database Data:", data)
if data:
    print("Data exists")
    print("Test Passed")
else:
    print("Test Failed")

conn.close()
