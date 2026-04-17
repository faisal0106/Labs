import sqlite3
print("Database checkpoint - Runtime record check")
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
user_id = int(input("Enter ID: "))
cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
data = cursor.fetchone()
print("Fetched Record:", data)
if data:
    print("Record Found")
    print("Test Passed")
else:
    print("Record Not Found")
    print("Test Failed")
conn.close()
