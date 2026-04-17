import sqlite3
import time as t
print("Database checkpoint - Custom check")
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM users WHERE id=1")
data = cursor.fetchone()
expected = "Faisal"
t.sleep(4)
print("Expected:", expected)
print("Actual:", data[0])
if data and data[0] == expected:
    print("Custom Check Passed")
else:
    print("Test Failed")
conn.close()
